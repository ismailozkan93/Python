#Geriye dönmeyen fonksiyonlara void fonksiyonlar denir
###Docstring
import math


def ustel_hesapla(sayi,üst):
    #ustel=sayi**üst
    ustel=math.pow(sayi,üst)
    return ustel
print(ustel_hesapla(3,5))
#math.pow dokumantasyonu
#math.pow?

#HAZIR METHODLAR VE ATTRIBUTELAR
#Python'da nesnelerin hazir metodlari ve hazir attributelari(özellikleri) vardir
#Bunlara kisayollardan erisilebilinir
print(ustel_hesapla.__doc__)
print(math.pow.__doc__)
#Pyhton'da built-in(hazir) olan iki alt tire(__)ile erisilen metod veya attributelara(özelliklere)
#DUNDER denir. DUNDER:DOUBLE UNDERSCORE

print(ustel_hesapla.__module__)
print(ustel_hesapla.__name__)


