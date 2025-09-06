import json

# === A. Membaca JSON lokal ===
with open("peminjaman_buku.json", "r", encoding="utf-8") as f:
    data = json.load(f)

dipinjam = 0
belum_kembali = 0

print("Belum kembali:")

for anggota in data["anggota"]:
    for pinjam in anggota["pinjam"]:
        dipinjam += 1
        if not pinjam["kembali"]:   # cek boolean, bukan string
            belum_kembali += 1
            print(f"- {anggota['nama']} : {pinjam['judul']} ({pinjam['tanggal']})")

print(f"\nTotal dipinjam: {dipinjam} | Belum kembali: {belum_kembali}")







#requests untuk ambil teks Arab & Inggris.

import requests
import textwrap
import arabic_reshaper
from bidi.algorithm import get_display

try:
    # Endpoint API
    url_ar = "https://api.alquran.cloud/v1/ayah/2:255/quran-simple"
    url_en = "https://api.alquran.cloud/v1/ayah/2:255/en.asad"

    # Ambil data dari API
    res_ar = requests.get(url_ar)
    res_en = requests.get(url_en)

    res_ar.raise_for_status()
    res_en.raise_for_status()

    data_ar = res_ar.json()
    data_en = res_en.json()

    ayat_ar = data_ar["data"]["text"]
    ayat_en = data_en["data"]["text"]

    # === RAPIKAN TEKS ARAB ===
    reshaped_text = arabic_reshaper.reshape(ayat_ar)      # bentuk huruf nyambung
    bidi_text = get_display(reshaped_text)                # dibalik jadi RTL benar

    # Bungkus teks biar rapi
    wrapper_ar = textwrap.TextWrapper(width=60)
    wrapper_en = textwrap.TextWrapper(width=70)

    print("Ayat Al-Kursi (2:255) - Arab:")
    print("\n".join(wrapper_ar.wrap(bidi_text)))

    print("\nTerjemah (EN):")
    print("\n".join(wrapper_en.wrap(ayat_en)))

except requests.exceptions.RequestException as e:
    print("Error saat mengambil data:", e)






