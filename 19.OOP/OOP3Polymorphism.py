"""
Polymorphism:
Cok sekillilik--> Bir arayüz (interface) farkli yerlerde farkli amaclar icin kullanilir

"""
class Kus:
    def __init__(self):
        print("Bird is created")

    def kimimBen(self):
        print("Ben bir kusum")

    def ucma(self):
        print("Kuslar ucabilir")

    def yuzme(self):
        print("Kuslar yüzebilir")


###Baykus--<Kustan kalitim aldi,--> ama bazi özelliklerini kendisine has
###child class--derived class

class Baykus(Kus):
      #Bir sinif hangi siniftan kalitim aliyorsa, parantez icinde ana sinif yazilir

    def __init__(self):
        super().__init__()      #önce ana sinifinin,super(), __init__() metodunu cagir
        print("Baykus is created")

    def kimimBen(self):
        print("Ben bir baykusum")

      # Baykus tüm kuslar gibi uctugu icin ucma() metodunu override etmeye (ezmek) gerek yok
      # Aynen kullaniriz
    def yuzme(self):
        print("Baykuslar yüzemez")
    #Baykusun gece görüsü vardir
    def gece_gorusu(self):
        print("Baykuslarin gece görüsü vardir")

##Kus ana sifindan kalitim alan bir kus daha
class Penguen(Kus):
    def __init__(self):
        super().__init__()  # önce ana sinifinin,super(), __init__() metodunu cagir
        print("Penguen is created")

    def kimimBen(self):
        print("Ben bir penguenim")

    def ucma(self):##Override etti --->üzerine yazdi,ezdi
        print("Penguenler ucamaz")

    #Penguenler yüzdügü icin -->yuzme() metodu ana class'ta kalsin

#Ayni siniftan (Kus) kalitim almis iki alt sinifimiz var(Baykus,Penguen)
#Polymorphism'i bir örnek ile görelim

#ortak arayüz
#ucmayi test eden bir fonksiyon

def ucabilir_mi(kus):
    #parametre olarak gelen kus nesnesinin ucma metodunu cagir
    kus.ucma()

#Simdi üc adet nesne  olusturalim
kus=Kus()
baykus=Baykus()
penguen=Penguen()

print("--------ucma testi--------")
#ucmayi test edelim
ucabilir_mi(kus)
ucabilir_mi(baykus)
ucabilir_mi(penguen)

#Bakin ucabilir_mi() Kus sinifi türünden
#bir nesne aldi ve onun ucma()metodunu cagirdi
#ucma metodu cagrildigi yere göre farkli davrandi
#iste ayni arayüzün farkli verilere göre farkli sonuclar vermesine
#POLYMORPHISM denir













