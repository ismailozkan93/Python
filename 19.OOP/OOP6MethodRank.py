"""
Cok seviyeli Kalitim:
Anneanne-->Anne-->Cocuk


"""
class AnneAnne(object):
    #Anneanne özelikleri
    pass

class Anne(AnneAnne):
    #Anneannenin özellikleri
    #Annenin kendi özellikleri
    pass
class Cocuk(Anne):
    #AnneAnne nin özellikleri
    #Annenin özellikleri
    #Cocugun özellikleri
    pass

#Saat de KumSaatinden kalitim alsin
#Saat ve Takvim-->SaatliTakvim ikisinden kalitim alan alt sinif

#Kum Saati
class Kumsaati(object):
    def __init__(self):
        print("Kum saati basladi")
    def kumSaatiBaslasin(self):
        print("Kum Saati baslasin")

class Saat(Kumsaati):
    """Saat'i simule eder"""
    def __init__(self,saat,dakika,saniye):
        super().__init__()
        self.saati_kur(saat,dakika,saniye)

    def saati_kur(self,saat,dakika,saniye):
        self.saat=saat
        self.dakika=dakika
        self.saniye=saniye

    def saat_kac(self):
        return "{0}:{1}:{2}".format(self.saat,self.dakika,self.saniye)

clock=Saat(0,0,0)
print(clock.saat_kac())
clock=Saat(10,4,28)
print(clock.saat_kac())

class Takvim(object):
    """Takvimi simule eder"""
    def __init__(self,d,m,y):
        self.takvim_kur(d,m,y)

    def takvim_kur(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y

    def bugun_ne(self):
        return "{d}:{m}:{y}".format(d=self.d,m=self.m,y=self.y)

takvim=Takvim(6,11,2019)
print(takvim.d)
print(takvim.m)
print(takvim.y)
print(takvim.bugun_ne())


#SaatliTakvim Class
class SaatliTakvim(Saat,Takvim):
    """
    Saat ve Takvimi beraber tutar
    """
    def __init__(self,d,m,y,saat,dakika,saniye):
        Saat.__init__(self,saat,dakika,saniye)
        Takvim.__init__(self,d,m,y)

#Bu kadar basit
print("----------------Saatli Takvim------------------")
saatli_takvim=SaatliTakvim(8,12,2020,16,45,7)
print(saatli_takvim.kumSaatiBaslasin())
print(saatli_takvim.saat_kac())
print(saatli_takvim.bugun_ne())

#Eger ayni metod bir kac atada varsa,hangisini calistirir?
#En yakin atasindan baslayarak cagirir
#Method Resolution Order-->MRO

print("Mro",SaatliTakvim.__mro__)
