#Objected Oriented Programming(oop)
#Nesne Tabanli Programlama
#Nesne-->etrafimizdaki hersey
#Python nesnelerin özellikleri
    #Öznitelikler(Attribute)
    #Davranisler(Behaviour)
#Penguen
#Öznitelikleri:adi,yasi,boyu,kilosu,rengi,turu...
#davranislari:yüzme,yürüme,sarki söyleme,danst etme...
#OOP:Kod tekrarini önlemek icin var
#DRY:Dont repeat yourself

"""
Class(Sinif):
Class bir nesnenin eskiz cizimidir.
Mimari cizimidir
Nesnenin neye benzeyecegini anlatir.
Örnek:Bina bir nesnedir,O binanin kagit üstündeki cizimi(mimari) class'dir
Penguen:
Kagida cizilmis bir penguen,cizim olan Sinifidir
O cizimden yapilmis gercek Penguen'de nesnedir
"""
"""
class Penguen:
    pass

Class yaratmak icin class anahtar kelimesi kullanilir.
TANIMLADIGIMIZ Class'imizin adi PENGUEN

Object(Nesne):
Nesne,Class'in hayat bulmus seklidir.(Instance)
Class'in ete kemige bürünmüs halidir
INSTANCE:Tekil olarak Olusturulmus bir NESNEDIR
nesne=Penguen()
"""

"""
Nesneler class'larin cagrilmasi ile olusturulur
"""
#Class Attribute:
#Bütün Penguenlerin ortak özellikleri vardir
#Bilimsel olarak türü(species)-->kus
#Class'tan üretilmis tüm varliklarda(nesne) ortak olan özelliklere "Class Attribute" denir.

#Instance Attribute
#Tekil bir nesneye özel nitelikler;
#Penguen,yasi,rengi,kilosu,boyu
"""
Method=Fonksiyon
Metod'lar Class icinde tanimlanan fonksiyonlardir
"""
class Penguen:
    #class attribute'lari(sinif özellikleri)
    tur="Kus"

    #Instance attributelari(varligin öznitelikleri)
    def __init__(self,ad,yas,renk):
        self.ad=ad
        self.yas=yas
        self.renk=renk
"""
self:O anda yaratilan nesneyi anlatir
"""
#2 adet Penguen Nesnesi olusturalim
kral=Penguen("Kral Penguen",4,"Turuncu")
sari_goz=Penguen("Sari Gözlü Penguen",1,"Kahverengi")

#Önce class attribute'larini print edelim
print(Penguen.tur)
print("{0}'in bilimsel türü:{1}".format(kral.ad,kral.__class__.tur))
print("{0}'in bilimsel türü:{1}".format(sari_goz.ad,sari_goz.__class__.tur))

#Instance Attributelarini print edelim
print("{0}'in yasi {1} ve rengi {2}".format(kral.ad,kral.yas,kral.renk))
print("{0}'in yasi {1} ve rengi {2}".format(sari_goz.ad,sari_goz.yas,sari_goz.renk))

#Attributelar--->"." nokta ile erisilir.
        #Class attribute ise -->.__class__.
        #Instance Attribute -->.
"""
__init__(self,....):
Bir class'tan nesne olusturulurken ilk cagrlan creator(yapici ve constructor) metoddur.
__init__() instance olusturur

*self : O anda yaratilmakta olan nesneyi anlatir.
Nesnenin özellikleri:
self.ad=....
self.renk=...
self.yas=...

Methodlar(DAVRANISLAR):
Method bir class icinde tanimlanmis foknsiyondur.
Nesnelerin davranisini anlatir.
"""
#Penguen Class'imiza metod ekleyelim
class Penguen:
    # class attribute'lari(sinif özellikleri)
    tur = "Kus"

    # Instance attributelari(varligin öznitelikleri)
    def __init__(self, ad, yas, renk):
        self.ad = ad
        self.yas = yas
        self.renk = renk

    #instance method(varligin metodu)
    def yuzme(self):
        return f"{self.ad} yüzebilir"

    def sarki_söyle(self,söyleyebilir_mi=False):
        if söyleyebilir_mi:
            return f"{self.ad} sarki söyleyebilir."
        else:
            return f"{self.ad} sarki söyleyemez."


    def dans_et(self,dans_edebilir_mi=False):
        if dans_edebilir_mi:
            return f"{self.ad} dans edebilir."
        else:
            return f"{self.ad} dans edemez."

#Yeni penguen nesneleri olustur
makaroni=Penguen("Makaroni Pengueni",8,"Sari")
print("{0}'in bilimsel türü {1}".format(makaroni.ad,makaroni.tur))
print("{0}'in yasi {1} ve rengi {2}".format(makaroni.ad,makaroni.yas,makaroni.renk))
print(makaroni.yuzme())
print(makaroni.dans_et())
print(makaroni.sarki_söyle())#makaroni.sarki_söyle(soyleyebilir_mi=True)-->Ma... eni sarki söyleyebilir

#Neseli Ayaklar penguenini olustur
neseli_ayaklar=Penguen("Neseli Ayaklar",1,"Gri-Papyon")

#Neseli Ayaklar yüzeyebilir
print(neseli_ayaklar.yuzme())

#Neseli Ayaklar Pengueni sarki söylemez
print(neseli_ayaklar.sarki_söyle(False))

#Neseli Ayaklar dans edebilir
print(neseli_ayaklar.dans_et(True))
