#soal pertama
kendaraan = ["mio", "motor", "200cc", "hitam", "roda 2" ]
#mencetak isi dari list kendaraan 
print(kendaraan)

#menambahkan value atau nilai di ujung list
#append 01
kendaraan.append("20.000.000.000")
#append 02
kendaraan.append("matic")
#cetak nilai kendaraan setelah perubahan 
print(kendaraan)

#menambahkan value setelah jenis kendaraan 
kendaraan.insert(2,"yamaha")
#cetak nilai kendaraan setelah perubahan 
print(kendaraan)

#soal kedua
pilihan = int(input("""Masukkan Pilihan Nomor: 
1. Menghitung Luas persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga
"""))

match pilihan:
    case 1:
        print("Menghitung Luas Persegi")
        s = int(input("Masukan Nilai Sisi: "))
        luaspersegi = s * s
        print(f"luas persegi dengan sisi {s} adalah  {luaspersegi}")
    case 2:
        print("Menghitung Luas Lingkaran")
        pi = 3.14
        r = int(input("Masukkan Nilai Jari Jari"))
        luaslingkaran = pi * r**2
        print(f"luas lingkaran dengan jari jari {r} adalah {luaslingkaran}")
    case 3:
        print("Menghitung Luas Segitiga")
        alas = int(input("Masukkan Nilai Alas: "))
        tinggi = int(input("Masukkan Nilai Tinggi: "))
        luasSegitiga = 1/2 * alas * tinggi
        print(f"luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luasssegitiga}")
    case _:
        print("Input Tidak Valid")