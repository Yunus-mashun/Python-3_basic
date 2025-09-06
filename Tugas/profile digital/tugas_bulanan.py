print("=========tugas bulanan=========")

nama = input("Nama lengkap : ")
umur = int(input("umur : "))
tahunsekarang = 2025
umurhitung = tahunsekarang - umur

kelas = input("kelas : ")
cita_cita = input("cita cita : ")
hobi = input("hobi faforit : ")
mood = input("lebih suka belajar pagi atau malam : ")

#g = input("kelas : ")
#print("perkenalkan")
#print("saya",a)
#print("umur saya",b)
#print("tinggi badan saya",d)
#print("saya dari",e)
#print("kota",f)
#print("saya sekarang kelas",g)
print("\n")


#print("=========tipe==========")
#print("pilih angka saja")
#print("\n")

#tipe = input("apa tipe digital kamu? :")
#print(tipe)

    
#if (tipe == "1"):
#    print("anak anime banget")

#elif (tipe == "2"):
#    print("ranked jalan terus")

#elif (tipe == "3"):
#    print("ngikutin gaya korea")

#elif (tipe == "4"):
#    print("tiktoker/youtuber wannabe")

#elif (tipe == "5"):
#    print("yang penting ngumpul")
#print("\n")

print("=============TIPE==============")
print("\n")

j = ["wibu","gamer","k-popers","anak konten","anak nongki"]
for i in j:
    print(i)
print("\n")
s = input("pilih salah satu sesuai kesukaan mu :")

if (s == "wibu"):
    tipe = "wibu"
    tanya =input("apa waifu atau husbando kamu? :")
    komentar = "tetap semangat nonton nya!"
elif (s == "gamer"):
    tipe = "gamer"
    tanya =input("apa game favorit kamu? :")
    komentar = "push rank terusss"
elif (s == "k-popers"):
    tipe = "k-popers"
    tanya =input("siapa bias kamu? :")
    komentar = "laamakk.. anak korea"
elif (s == "anak konten"):
    tipe = "anak konten"
    tanya =input("Platform favorit kamu? TikTok? YouTube? :")
    komentar = "tetap semangat ngontennya" 
elif (s == "anak nongki"):
    tipe = "anak nongki"
    tanya =input("Nongkrong paling sering di mana? :")
    komentar = "ingat nabung cuyy "
print("\n")

print("===========FUN CHECK==================")
print("\n")

soal = input("teman di sebelah mu bau ya? :")

if (soal == "ya"):
    jawaban = "teman disebelah mu bau ya? : ya"
    print("waduuuhh.. baunya nyengat sekalii...")
    saran = "suruh dia mandi dong"

else:
    jawaban = "teman disebelah mu bau ya? : tidak"
    print("baguslah kalau begitu..")
    saran = "berarti dia bukan orang malas"
print("\n==== OUTPUT ====")

print("\n===== PROFIL DIGITAL KAMU =====")
print(f"Nama : {nama}")
print(f"Umur : {umur}")
print(f"tahunlahir:{umurhitung}")
print(f"kelas : {kelas}")
print(f"hobi : {hobi}")
print(f"cita cita : {cita_cita}")
print(f"tipe belajar : {mood}")

print("\n=== TIPE DIGITAL ===")
print(f"tipe : {tipe}")
print(f"{tanya}")
print(f"komentar : {komentar}")

print("\n=== FUN CHECK ===")
print(f"{jawaban}")
print(f"{saran}")





















