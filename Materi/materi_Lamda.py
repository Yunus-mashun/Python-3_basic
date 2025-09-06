print("==========lamda========")
#def funsi lebih dari satu baris
def halo_dek(nama):
    print(f"halo dek {nama}")
    print(f"apa kabar dek {nama}")
    print("---------------")
#prbedaan sama def
halo_kak = lambda nama :print(f"halo kak {nama}") 
#fungsi tidak akan berguna jika tidak dipanggil
halo_dek("nezuko")
halo_dek("anya")
halo_kak("bilal")
halo_kak("yunus")
halo_kak("laylaa")


# higher order function (map, sorted, filter)
uang_jajan = [100000, 50000, 20000, 75000, 3000]
# map() -> mentransformasi data item
kurangi_jajan = map(lambda uang: uang - 5000, uang_jajan)
tambah_jajan = map(lambda uang: uang + 10000, uang_jajan)
list_kurangi_jajan = list(kurangi_jajan)
list_tambah_jajan = list(tambah_jajan)
print(f"\nuang jajan santri: {uang_jajan}")
print(f"uang jajan dikurangi: {list_kurangi_jajan}")
print(f" kalo rajin uangnya ditambah: {list_tambah_jajan}")
print("-------------------------")

#sorted() -> untuk mengurut kan data
urutkan = sorted(uang_jajan)
balik_uang = sorted(uang_jajan, reverse=True)
print(f"\nurutkan uang: {urutkan}")
print(f"urutan uang terbalik : {balik_uang}")
print("-----------------------------")



#filter() -> menyaring data sesuai kondisi
filter_uang_gede = filter(lambda uang: uang > 50000, uang_jajan)
list_uang_gede = list(filter_uang_gede)
print(f"\nuang yang besar: {list_uang_gede}")


# module 


























































