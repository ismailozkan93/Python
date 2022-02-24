##Fonksiyonlarin Dönüs Degeri olarak Tuple'lar
#Fonksiyonlari islerken fark etmis olabilirsiniz,fonksiyon geriye sadece bir deger döner
#BIRDEN FAZLA DEGER dönmesi icin TUPLE() dönmemiz yeterli
#Örnegin Python un standart divmod() fonksiyonu iki parametre alir
#Bölen ve bölünen
#geriye bölüm ve kalan seklinde tuple döner

sonuc=divmod(23,4)
print(sonuc,type(sonuc))
bolum=sonuc[0]
kalan=sonuc[1]
print(bolum,kalan)

##Parametre sayisi belli olmayan bir fonksiyon yazin
#*args ile sayisi belli olmayan coklu parametre alabilir
def toplam_ve_carpim(*args):
    print(type(args))
    print(args)

toplam_ve_carpim(2,5,6,4)
#args yapisi aslida bir tuple'dir

def toplam_ve_carpim1(*args):
    toplam=sum(args)## toplam sum()
    carpim=1
    for a in args:
        carpim=carpim*a

    return (toplam,carpim)

print(toplam_ve_carpim1(2,3,4,5))
#Paramaetre olarak bir tamsayi listesi alan ve bu listenin minumum,maksimum ve aritmetik ortalama deger döner fonksiyon

def min_max_ort(*args):
    minumum=min(args)
    maximum=max(args)
    ortalama=sum(args)/len(args)
    return (minumum,maximum,ortalama)

print(min_max_ort(2,6,8,10))

#2NCI YOL
##Ortalama(mean) fonksyionu icin statistics yani istatistik paketini kullanin
#Modülü import etmek icin ->import
import statistics
def basit_islem(liste):
    minumum=min(liste)
    maksimum=max(liste)
    ortalama=statistics.mean(liste)
    return (minumum,maksimum,ortalama)

liste=[1,2,3,4,5]
minumum,maximum,ortalama=basit_islem(liste)
print(minumum,maximum,ortalama)




























##