


##Class'i taniyalim
#docstring--->class
#import math


class Araba:
    """
    Bu araba classidir
    """
    marka="BMW"

    def calisma(self):
        print("Araba calisiyor")

#Marka attribute erismek icin nesne olusturmaya gerek yoktur
#Nesne olusturmadan -->direk class ile olusturmak
print(Araba.marka)

"""
dunder (double underscore):
Iki alt tire  (__) metodlara ve attributelara "DUNDER" adi verilir
"""
#tanimladigimiz araba classinin docstringine ulasalim
print(Araba.__doc__)
print(Araba.calisma)
#print(Araba.calisma())--->NESNE OLUSTURMADAN CAGIRAMAYIZ

yeni_araba=Araba()
print(yeni_araba.calisma())#Self parametresi vermedik
print(yeni_araba.marka)     #Self parametresi yeni arabanin kendisi

#ilk parametre self ise -->Araba.calisma(yeni_araba)
Araba.calisma(yeni_araba)
print("**************************************")

#import Math
class Cember:
    def __init__(self,yaricap):
        self.__yaricap=yaricap

    def get_yaricap(self):
        return self.__yaricap

    def set_yaricap(self,yeni_yaricap):
        if yeni_yaricap>0:
            self.__yaricap=yeni_yaricap

        else:
            print("Yaricap pozitif olmali")

    def cevre(self):
        return (22/7)*self.__yaricap**2

cember_1=Cember(10)
print(cember_1.get_yaricap())
print(cember_1.cevre())
print("-------SET---------")
cember_1.set_yaricap(20)
print(cember_1.get_yaricap())
print(cember_1.cevre())

#Yeni bir sinif
class Ogrenci:
    def __init__(self,isim,yas,sinif):
        self.isim=isim
        self.yas=yas
        self.sinif=sinif


ogr=Ogrenci("Cin Ali",8,"3-A")
print(ogr.isim)
print(ogr.yas)
print(ogr.sinif)


#Nesnelerin attributelarini silelim.-->Del
del ogr.yas
#Nesnenin kendisini silme
#del ogr




















