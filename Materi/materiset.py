print("materi set")
print("------------------------------")

# set-> { } -> tidak berurutan, berubah, tidak duplikat
buah = {"nanas","semangka","jambu"}
buah1 = {"pepaya","mangga","markisa"}
print("\n buah ucok : ",buah)
print("\nbuah adi : ",buah1)
buah.add("pisang")
buah.add("nanas")#jika sudah ada maka akan di skip
buah1.add("nanas")
print("\nbuah ucok sekarang : ",buah)
print("\nbuah adi sekarang : ",buah1)
# remove() => menghapus item pada set
buah1.remove("pepaya")
print("\npunya adi di kurang : ",buah1)
# len() => menghitung jumlah item
print("\nbuah ucok ada",len(buah),"=>",buah)
print("\nbuah adi ada",len(buah1),"=>",buah1)

# .union() menggabungkan 2 set yang berbeda
buah_gabungan = buah.union(buah1)
total_buah = len(buah_gabungan)
print("\nbuah gabungan :",total_buah,"=>",buah_gabungan)

#.intersection() mencari item yang sama dari 2 set
buah_kembar = buah.intersection(buah1)
print("\nbuah kembar : ",buah_kembar)

#.difference() mencari item yang beda dari 2 set
buah_beda = buah.difference(buah1)
print("\nbuah beda : ",buah_beda)













# dict (dictionary) -> {key:value}/{kunci:isinya}
# berurutan berdasarkan key, berubah, key tidak duplikat

daftar_hero = {
    "hero 1": "upin",
    "hero 2": "ipin",
    "hero 3": "ijat",
    "hero 4": "jarjit",
    "jurus": {
        "jurus 1": "terbang",
        "jurus 2": "lari kencang",
        "jurus 3": "menghilang",
    }
}

print("\nDAFTAR HERO:",daftar_hero)
print("\nHERO PILIHAN:",daftar_hero["hero 3"])
print("\nJURUS ANDALAN:",daftar_hero["jurus"]["jurus 2"])


#mengubah item value berdasarkan key
daftar_hero["hero 3"] = "mail"
daftar_hero["jurus"]["jurus 2"] = ["lompat tinggi"]
print("\nHERO BARU:",daftar_hero["hero 3"])
print("\nJURUS BARU:",daftar_hero["jurus"]["jurus 2"])

#menambah item value berdasarkan key
daftar_hero["hero 5"] = ["ijat"]
print("\nHERO BARU LAGI:",daftar_hero["hero 5"])
