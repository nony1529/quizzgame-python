#Project 1
#Quiz Game Python
#Nony Zeina

#Membuat Pertanyaan
pertanyaan = ("Berapa jumlah provinsi di Indonesia?: ",
"Apa nama mata uang resmi negara Indonesia?: ",
"Siapakah Presiden pertama di Indonesia?: ",
"Apa nama ibu kota Jawa Barat?: ",
"Berapa banyak sila dalam Pancasila?: ")

#Membuat Pilihan Jawaban
pilihan = (("A. 34", "B. 38", "C. 36", "D. 37"),
("A. Rupiah", "B. Yen", "C. Dollar", "D. Euro"),
("A. Joko Widodo", "B. Soeharto", "C. Megawati Soekarnoputri", "D. Soekarno"),
("A. Surabaya", "B. Jakarta", "C. Bandung", "D. Cianjur"),
("A. 6", "B. 7", "C. 5", "D. 4"))

#Menentukan Jawaban
jawaban = ("B", "A", "D", "C", "C")
menebak = []
skor = 0
nomor_pertanyaan = 0

#Menampilkan Pertanyaan
for pertanyaan1 in pertanyaan:
    print("=" * 43)
    print(pertanyaan1)
    for pilihan1 in pilihan[nomor_pertanyaan]:
        print(pilihan1)

#Input Jawaban Dan Menampilkan Jawaban
    menebak1 = input("Pilih (A, B, C, D) : ").upper()
    menebak.append(menebak1)
    if menebak1 == jawaban[nomor_pertanyaan]:
        skor += 1
        print("BENAR")
    else:
        print("TIDAK BENAR")
        print(f"{jawaban[nomor_pertanyaan]} Ini Jawaban Yang Benar")

    nomor_pertanyaan += 1

#Tampilan Skor
print("=" * 45)
print("\t\tHASIL JAWABAN")
print("=" * 45)

#Menampilkan Apa Saja Yang Kita Jawab
print("Tebakan Anda\t  = ", end="")
for menebak1 in menebak:
    print(menebak1, end =" ") 

#Menampilkan Skor
skor = int(skor / len(jawaban) * 100)
print(f"Skor Kamu Adalah = {skor}%")