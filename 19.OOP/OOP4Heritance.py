"""
Ana Sinif(Base Class)
    -Alt Sinif 1(Child Class)
    -Alt Sinif 2(Child Class)
"""
class AnaSinif:
    #Ana Sinifin Özelikleri
    pass

class AltSinif1(AnaSinif):
    #Ana Sinifin Özellikleri
    #Alt Sinif1in özellikleri
    pass

class AltSinif2(AnaSinif):
    #Ana Sinifinin Özellikleri
    #Alt Sinif 2'in Özellikleri
    pass

#-->Örnek-->Sekil
import math
#super class
class Sekil:
    """Sekiller icin super class"""
    def __init__(self,renk="kirmizi"):
        self.renk=renk

#sub class-->Daire
class Daire(Sekil):
    """Daire sinifi,sekil sinifindan kalitim yapar"""
    def __init__(self,yaricap,renk="Mavi"):
        super().__init__(renk=renk)
        self.yaricap=yaricap

    def alan(self):
        return math.pi*self.yaricap**2

class Dikdörtgen(Sekil):
    """Dikdörtgen Sinifi"""
    def __init__(self,kisa=1.0,uzun=1.0,renk="turuncu"):
        super().__init__(renk=renk)
        self.kisa=kisa
        self.uzun=uzun

    def alan(self):
        return self.kisa*self.uzun

class Kare(Sekil):
    """Kare Sinifi"""
    def __init__(self,kenar=1.0,renk="beyaz"):
        super().__init__(renk=renk)
        self.kenar=kenar
        return kenar**2

#Nesne olustur
#Sekil
se=Sekil("mor")
print("Sekil nesnesi olan se'nin rengi:",se.renk)
#Daire
da=Daire(yaricap=5)
print("Daire nesnesi olan da'nin yaricapi",da.yaricap)
print("Daire nesnesi olan da'nin rengi",da.renk)#AttributeError: 'Daire' object has no attribute 'renk'
#Daireyi olustururken --> super().__init__() metodunu cagirmadik##Cagirinca default renk=kirmizi gelir
                          #super().__init__(renk=renk)mavi gelir

#DIKDÖRTGEN
dk=Dikdörtgen(kisa=2, uzun=8,renk="sari")
print("Dikdörtgenlerin nesnesi olan dk'nin rengi: ",dk.renk)
print("Dikdörtgenin Alani: ",dk.alan())

"""
Object class'i 
Python'da bütün classlarin atasi, "object" class'idir
Tüm siniflar "object" sinifindan gelir
"""
#class Sekil:--> class Sekil(Object)
print("Sekil Sinifi, object sinifinin alt sinifi mi?: ",isinstance(se,object))

#issubclass()
#Kare,Sekil'in alt sinifi mi?
print("Kare,Sekil'in alt sinifi mi?",issubclass(Kare,Sekil))


























