class Animal:
    print("==========Panda==========")
    def __init__(self, nama, makanan, hidup, berkembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak
    def cetak(self):
        print("\nNama \t\t :", self.nama,
              "\nMakanan \t :", self.makanan,
              "\nHidup \t\t :", self.hidup,
              "\nBerkembangbiak \t :", self.berkembangbiak)

objek = Animal ("Panda", "Bambu", "Darat", "Beranak") 
objek.cetak()