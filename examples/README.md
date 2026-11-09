# Pakej Pembaca Boleh Laksana

Jalankan semua arahan dari akar projek yang diekstrak. Import modul menggunakan `examples.*`.
Prompt penggredan ialah `prompts/grades-developer.md` dan `prompts/grades-qa.md`; `prompts/qa.md` khusus untuk laman web. Jalankan latihan dalam salinan sendiri supaya versi rujukan kekal utuh.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
.venv/bin/python -m examples.pipeline
```

| Bab | Titik mula | Fokus penerimaan |
|---|---|---|
| 1 | `calculator.py` | Aritmetik, pembahagian sifar dan jenis data |
| 2 | `grades.py` | Julat markah, mata pelajaran hilang dan kedudukan seri |
| 3 | `../scripts/probe_herdr.py --live` | Jalankan, baca, tunggu dan bersihkan panel shell baharu |
| 4 | `../scripts/team.py` | Tugasan berperingkat, ID tugas unik dan penerimaan artifak |
| 5 | `prompts/reviewer-a.md`, `reviewer-b.md` | Semakan bebas dan keputusan Pengurus |
| 6 | `handoff.py` | Kewujudan fail, skop projek dan SHA-256 |
| 7 | `task_manager/` | CRUD, pengesahan, halaman statik dan data kekal selepas mula semula |
| 8 | `research.py` | Dakwaan, sumber, petikan dan ketidakpastian |
| 9 | `pipeline.py` | Kod keluar, had masa, penerimaan dan henti apabila gagal |
| 10 | `queue.py` | Nyahpendua, lease, pemulihan, dead letter dan serentak |

Mulakan laman web:

```bash
.venv/bin/python -m uvicorn examples.task_manager.main:app --host 0.0.0.0 --port 8000
```

Buka `http://localhost:8000/` dalam pelayar Windows melalui WSL. Data latihan disimpan secara lalai di `examples/data/tasks.db`; ujian automatik menggunakan direktori sementara.

Baris gilir latar ialah contoh pengiraan terhad yang tidak memanggil model berbayar. Penugasan model sebenar dinyatakan secara jelas dalam `scripts/team.py`; pasang dan log masuk ke CLI berkenaan dahulu.
