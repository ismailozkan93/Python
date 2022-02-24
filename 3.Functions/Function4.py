#Parametreler(Argümanlar)
#Cogu zaman fonksiyonlar parametreler ihtiyac duyarlar
#(***Parametreler***) fonksiyonun calismasi icin kendisine iletilen girdilerdir
#Parametreler fonksiyon cagrilirken iletilir

def karesini_yaz(sayi):
    karesi=sayi**2
    print(karesi)

karesini_yaz(5)
#2 PAREMETRE alan fonksiyon
def dikdörtgen_alan(a,b):
    alan=a*b
    print(alan)

dikdörtgen_alan(5,7)

kisa=6
uzun=8
dikdörtgen_alan(kisa,uzun)

def ogrenci_ilk_adi(ilk_adi):
    print("Adi: "+ilk_adi)
def ogrenci_soyadi(soyadi):
    print("Soyad: "+soyadi)
def ogrenci_yas(yas):
    print("Yas: "+str(yas)) #str---int i strye ceviririz
def ogrenci_dil(dil):
    print("Dil: "+dil)



def ogrenci_bilgileri(ilk_adi,soyadi,yas,dil):
    ogrenci_ilk_adi(ilk_adi)
    ogrenci_soyadi(soyadi)
    ogrenci_yas(yas)
    ogrenci_dil(dil)

ogrenci_bilgileri("Klar","Kent",34,"Python")