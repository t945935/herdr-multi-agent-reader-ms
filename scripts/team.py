#!/usr/bin/env python3
"""Hantar tugas kepada ejen idle yang telah dimulakan dan sahkan resit khusus tugas."""
import argparse
import json
import os
import subprocess
import uuid
from pathlib import Path


def call(*args, timeout=310):
    done = subprocess.run(["herdr", *args], text=True, capture_output=True, timeout=timeout)
    if done.returncode:
        raise RuntimeError(done.stderr or done.stdout)
    return json.loads(done.stdout)["result"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    parser.add_argument("prompt", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if os.environ.get("HERDR_ENV") != "1":
        raise SystemExit("Jalankan dalam Herdr")
    agent = call("agent", "get", args.target)["agent"]
    if agent["agent_status"] not in {"idle", "done"}:
        raise SystemExit("Ejen mesti idle/done sebelum tugasan bermula")
    path = args.output.resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit("Pilih laluan resit baharu; jangan guna semula tugas lama")
    task_id = uuid.uuid4().hex
    prompt = args.prompt.read_text() + (
        f"\n\ntask_id tugas ini ialah {task_id}\nlaluan_selesai={path}\n"
        'Selesaikan tugasan sebenar, kemudian tulis JSON: {"task_id":"pengecam di atas","status":"completed",'
        '"summary":"hasil kerja khusus dan pengesahan","artifacts":["laluan artifak sebenar"]}。'
        "Jika tugasan tidak dapat diselesaikan, gunakan status=blocked dan jelaskan sebabnya dalam summary. Jangan mulakan ejen lain."
    )
    settled = call("agent", "prompt", args.target, prompt, "--wait", "--timeout", "300000")
    state = settled["agent"]["agent_status"]
    if state not in {"idle", "done"} or not path.is_file():
        raise SystemExit("Ejen selesai tanpa resit yang diterima; periksa agent get/read")
    receipt = json.loads(path.read_text())
    if receipt.get("task_id") != task_id or receipt.get("status") != "completed" or not receipt.get("summary"):
        raise SystemExit("Resit tidak menerima tugasan ini")
    for artifact in receipt.get("artifacts", []):
        candidate = Path(artifact)
        if not candidate.is_absolute():
            candidate = Path.cwd() / candidate
        if not candidate.is_file():
            raise SystemExit(f"Artifak tiada: {artifact}")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
