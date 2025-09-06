import csv

# = 
# Baca semua data dari dari csv

with open("keuangan.csv",newline="",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)

# 1. tampilkan Semua Data
print("\n")

print("📌 Semua Data: ")
for row in data:
    print(f"{row['Tanggal']} | {row['Keterangan']} | {row['Kategori']} | {row['Jumlah']}")

print("🏹" * 20)

# 2. Hitung Total Pengeluaran
print("\n")

total = sum(int(row["Jumlah"]) for row in data)
print(f"💰 Total Pengeluaran: Rp.{total}")