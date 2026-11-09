# Pakej Sumber Pembaca Herdr — Bahasa Melayu Malaysia

Pakej ini mengandungi contoh rujukan, ujian dan prompt peranan untuk buku *Aliran Kerja Berbilang Ejen yang Boleh Dipercayai dengan Herdr*.

## Keperluan dan pemasangan

Python 3.12 disyorkan. Ujian luar talian tidak memerlukan akaun model; latihan ejen langsung memerlukan Herdr TUI dan CLI ejen yang telah dikonfigurasikan. Jalankan arahan berikut dari direktori akar pakej yang diekstrak:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
```

Keputusan rujukan: `42 passed`. Untuk mengesahkan ZIP, jalankan `sha256sum -c SHA256SUMS.txt` di dalam direktori yang mengandungi fail checksum. Jangan masukkan token, kunci API atau pangkalan data sebenar ke dalam pakej.

Sumber ini disediakan sebagai bahan pelengkap edisi Bahasa Melayu Happy eBook. Lihat `RIGHTS.md`; tiada lesen umum atau lesen MIT diberikan.
