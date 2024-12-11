from Animal import *
print("\n==========Cobra==========")
class Cobra(Animal):
    def __init__ (self, nama, makanan, hidup, berkembangbiak, bisaular, design):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.bisaular = bisaular
        self.design = design

    def cetak_Cobra(self):
        super().cetak()
        print("Bisaular \t :", self.bisaular, 
              "\nDesign Ular \t :", self.design)

Ular = Cobra("Cobra", "Daging", "Darat", "Bertelur", "Berbisa", "Bulat-Bulat")
Ular.cetak_Cobra()

from Animal import *
print("\n==========Channa==========")
class Channa(Animal):
    def __init__ (self, nama, makanan, hidup, berkembangbiak, jenis, corak):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.jenis = jenis
        self.corak = corak

    def cetak_Channa(self):
        super().cetak()
        print("Jenis  \t\t :", self.jenis, 
              "\nCorak \t\t :", self.corak)

Ikan = Channa("Channa", "Cacing", "Air", "Bertelur", "Barca", "Bintik bintik hitam")
Ikan.cetak_Channa()

from Animal import *
print("\n==========Merpati==========")
class Merpati(Animal):
    def __init__ (self, nama, makanan, hidup, berkembangbiak, jenis, asal):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.jenis = jenis
        self.asal = asal

    def cetak_Merpati(self):
        super().cetak()
        print("Jenis  \t\t :", self.jenis, 
              "\nAsal \t\t :", self.asal)

Burung = Merpati("Merpati", "Biji-bijian", "udara", "Bertelur", "Spinifex", "Australia")
Burung.cetak_Merpati()