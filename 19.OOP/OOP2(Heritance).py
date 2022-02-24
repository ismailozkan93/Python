#Kalitim(Inheritance)
#Aynen gercek hayattaki gibi OOP'DE class birbirinden kalitim alabilirler
#Kalitim Alan CLass-->CHILD CLASS,DERIVED CLASS
#Kalitim Veren Class
#Kalitim Veren Class-->Parent Class,Base Class(Ana Class)

#Kus sinifini olusturalim
class Kus:
    def __init__(self):
        print("Bird is created")

    def kimimBen(self):
        print("Ben bir kusum")

    def ucma(self):
        print("Kuslar ucabilir")

    def yuzme(self):
        print("Kuslar yüzebilir")

#Bir kus nesnesi olustur
#minikkus=Kus()
#minikkus.kimimBen()
#minikkus.yuzme()
#minikkus.ucma()

#Kus türleri icin bir ana class'imiz var
#Baykus da bir kus--> child

#child class--derived class
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

#kucuk_baykus=Baykus()
#kucuk_baykus.kimimBen()
#kucuk_baykus.ucma()
#kucuk_baykus.yuzme()
#kucuk_baykus.gece_gorusu()

"""
Encapsulation(Gizleme):
OOP'de disaridan direkt olarak bizim classimiz icindeki
attributelara erisilmesini istemeyebiliriz
Atrribute gizleme:"__" ile yapilir
Iki alt tireli(__<name>)Private olmus olur
"""

#Örnegin bir Telefon sinifimiz olsun
class Telefon:
    def __init__(self):
        #telefonun standart fiyatini belirleyelim
        self.__fiyat=1000

    def sat(self):

        print("Satis fiyati: {} TL".format(self.__fiyat))

    def set_fiyat(self,yeni_fiyat):
        # KONTROL-->FIYAT NEGATIF MI
        if yeni_fiyat<=0:
            print("Negatif Fiyat Olamaz")
        else:
            self.__fiyat=yeni_fiyat

    def get_fiyat(self):
        return self.__fiyat

tel=Telefon()
#print(tel.__fiyat)      #no attribute
#Cünkü __fiyat-->Private

#Telefon sat
tel.sat()

#Telefon Fiyatlarini elle (disaridan) degistirmeye calissak
tel.__fiyat=5000

#telefon sat
tel.sat() #1000
#tekrarlar 1000 Tl gelmesinin sebebi -->tel.__fiyat--> classin icindeki __fiyat degil
print(tel.__fiyat)#5000

#nesneye class'tan bagimsiz bir olarak özellikler verebilirsiniz
tel.renk="Siyah"
print(tel.renk)#Python'da herhangi bir nesneye disaridan(class'tan bagimsiz) özellik verebilirsiniz
               #Ama bu özellik class'a yansimaz

#Fiyati gercekten set etmek istersek(tanimlamak)istesek
tel.set_fiyat(8000)
tel.sat()

#sadece fiyati görmek istiyorum-->get_fiyat
fiyat=tel.get_fiyat()
print(fiyat)
"""
Get-Set Metodlari-->Getter-Setter
Class'in private attributelari icin alma ve set etme islemlerini yapar
"""
"""
Peki neden Encapsulation?
Kontrolün Class'ta olmasi icin var
Set Metodunda KONTROL yapilir
"""
#Örnek
#Fiyati -2000Tl vermek isterse
tel.set_fiyat(-2000)
print(tel.get_fiyat())



























