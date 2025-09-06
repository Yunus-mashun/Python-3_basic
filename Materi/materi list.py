# list = laci
print("materi 6c python data pictures")
print("------------------------------")
# list -> [] -> berurutan, berubah boleh duplikat
daftar_belanja = [
"es teh desa", # index 0 
"cilok",#index 2
"es kopi",# index 3
]
print("tas belanja :",daftar_belanja)

#------------------------------
# untuk mengambil salah satu item
# akses item dengan index
print(daftar_belanja[1])
#------------------------------

# append() untuk menambah item ke akhir list
daftar_belanja.append("tahoo golek")
daftar_belanja.append("olive")
daftar_belanja.append("kebab")
# insert() untuk menambah item pada index tertentu
daftar_belanja.insert(1,"sambel udang")
daftar_belanja.insert(3,"burger")
daftar_belanja.insert(2,"telor gulung")
# remove() untuk menghapus item
daftar_belanja.remove("es teh desa")
daftar_belanja.remove("es kopi")
print("tas belanja skrg :",daftar_belanja)
print("\n yang enak :",daftar_belanja[3])

# menggabungkan list dengan +
laci1 = ["kurma","apel","pisang","lemon"]
laci2 = ["jeruk","jambu","semangka"]
gabung = laci1 + laci2
#yang di-print fariabel gabungan nya
print("selruruh buah:",gabung)

# menggandakan item dengan *
print("pendapatan :",laci1 * 3)

print("---------------------")
# list bercabang (list multi dimensi)
daftar_menu = [
  ["kopi","teh","susu"],
  ["jus jeruk","jus mangga","jus anggur"],
  ["es teler","es campur","es dawet"],
]
print("DAFTAR MENU:",daftar_menu)
print(daftar_menu[1][2])
print(daftar_menu[2][0])
print("_---------------------_")
# Tuppel -> ( ) ->berurutan, tidak berubah, boleh duplikat
ttl = ("cirebon", 19, "agustus", 2010)
print("TTL :",ttl)
print("bulan lahir saya:",ttl[2])
# unpacking variable (mengekstrak tuple ke variable baru sesuai urutan)
tempat_lahir, tanggal_lahir, bln_lahir, thn_lahir = ttl
print("Thn lahir:",thn_lahir)
print("--------------------")


print("\n")
#-----------------------
#pop menghapus dengan index
print(daftar_belanja)
daftar_belanja.pop(2)
print(daftar_belanja)
print("perbedaan ada di index 2")
#-----------------------
print("\n")


for i in daftar_belanja:
    print(i)








