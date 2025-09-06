print("\n-----PERMAINAN JSON------")

import json


file_data_json = r"pekan3/file.json"

with open(file_data_json,"r") as file_json:
    baca_json = json.load(file_json)
    list_json = list(baca_json) # ubah csv object ke list
    print(f"\nJudul file : {baca_json['judul']}")
    print(f"Jumlah rukun islam : {baca_json['jumlah']}")
    print("DAFTAR RUKUN ISLAM : ")
    for item_rukun in baca_json['rukun']:
        print(item_rukun)
    print("-" * 45)




    print("\n MAU BUAT TABEL")
    print("-" * 45)
    print("daftar 3 surah dalam Al-Qur'an")
    print("-" * 45)
    print("| NO | NAMA | JUMLAH AYAT | TEMPAT TURUN |")
    print("-" * 45)
    # tampilkan surah surah sebagai tabel
    # keys : nomor, nama, jumlah_ayat, tempat_turun
    for surah in baca_json['surah']:
        print(f" | {surah['nomor']} | {surah['nama']} | {surah['jumlah_ayat']} | {surah['tempat_turun']} | ")


# PASTIKAN FILE YANG DIOLAH SUDAH DIIMPORT !



















































