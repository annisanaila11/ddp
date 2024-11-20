#soal nomer 01
print('---- mencari celcius ke farenheit ----')
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

# soal nomer 02
print('---- mencari bilangan genap ----')
def is_genap(bilangan_genap):
    return bilangan_genap %2 == 0

print(is_genap(4))
print(is_genap(7))

#soal nomer 03
print('---- membuat keterangan kelulusan ----')
def nilai(nilai_kelulusan):
    if nilai_kelulusan >= 70:
        return 'Lulus'
    else :
        return 'Tidak Lulus'

#untuk mencetak value
print(nilai(80))
print(nilai(60))

#soal nomer 04
print('---- mencetak bilangan ganjil ----')
def bilangan(ganjil):
    for i in range (1, ganjil, 2):
        print(i, end=" ")

#untuk memeasukan value
bilangan(20)




