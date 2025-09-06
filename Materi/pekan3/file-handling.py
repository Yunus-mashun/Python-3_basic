import csv

print("materi 10 - FILE HANDLING")
print("_-------------------------_")
# file extension/ekstensi yang membedakan jenis file satudan lainnya, lihat diakhir nama file
# .py (python), doc.(document), .txt (text file)
# cari posisi file yang mau dibuka

file_path = r"C:\New folder\pekan3\pesan.txt"
#buka file target dengan mode tertentu

file_pesan = open(file_path, "r") # r = read only
# fungsi read() = membaca semua isi file

baca_pesan = file_pesan.read()
print(f"isi pesanku: \n{baca_pesan}")

#tutup file
file_pesan.close()

print("\n-------OPEN FILE CSV---------")
print("=============================")

# buka file dengan mode "r" (read/baca)
csv_apa_path = r"C:\New folder\pekan3\apa.csv"

with open(csv_apa_path,"r") as file_alamat:
    baca_alamat = csv.reader(file_alamat)
    list_alamat = list(baca_alamat) # ubah csv object ke list
    print(f"daftar alamat: {list_alamat}")


print("\n----------ADD ROW CSV----------")
alamat_kholid = [7,"khalid","sukabumi"]
print(f"Alamat baru: {alamat_kholid}")

with open(csv_apa_path, "a", newline="") as file_alamat:
    tulis_alamat = csv.writer(file_alamat)# targetkan file
    tulis_alamat.writerow(alamat_kholid)# tambah alamat baru

print("--> selesai menambah alamat baru ke csv")


print("\n-------------------update row csv--------------------")
#open --> baca file --> ambil datanya , jadikan list
#ekstrak data dengan loop (edit/hapus)
#buat ulang semua baris file csv dengan mode "w"

csv_apa_path = r"C:\New folder\pekan3\apa.csv"
#buat list kosong untuk menampung data dari csv
data_alamat = []

with open(csv_apa_path,"r") as file_alamat:
    baca_alamat = csv.reader(file_alamat)
    for item_alamat in baca_alamat:
        data_alamat.append(item_alamat)

#ekstrak list data alamat dengan for loop
for item in data_alamat:
#cek kolom nama (index 1)
  if item[1] == 'AGUS':
      print("data AGUS ditemukan, ganti alamatnya....")
      item[2]= "bandung" # index 2 (kolom alamat)  
  else:
      print(" skipp... bukan data Ridho!!!")


#hapus data dari csv berdasarkan index
del data_alamat[4]

# ubah data alamat (index 2)
print(f"\n list data alamat: {data_alamat}")

print("\n---------------- mode (w)-------------")

with open(csv_apa_path, "w", newline="") as file_alamat:
    tulis_alamat = csv.writer(file_alamat)# targetkan file
    tulis_alamat.writerows(data_alamat)# tambah baris baru
    print(" \n --> selesai membuat ulang data csv")


print("--------heandling-----------------")




















