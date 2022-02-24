import math

def alan(yaricap):
        return math.pi * yaricap ** 2

def uzaklik(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        print("dx:", dx)
        print("dy:", dy)
        kareler_toplam = dx ** 2 + dy ** 2
        print(kareler_toplam)
        return math.sqrt(kareler_toplam)

def iki_noktadan_gecen_daire_alani(x1,y1,x2,y2):
    """
    yaricapi verilen iki nokta arasi olan bir dairenin alanini hesaplar
    Parametreler:
        *x1:int,birinci noktanin x koordinati
        *y1:int,brinci noktanin y koordinati
        *x2:int,ikinci noktanin x koordinati
        *y2:int,ikinci noktanin y koordinati
    dönüs:Darienin alani
    """
    #yaricai hesaplayalim
    r=uzaklik(x1,y1,x2,y2)
    print("r",r)
    #alani hesapla
    a=alan(r)
    print("a",a)

    return a
iki_noktadan_gecen_daire_alani(1,3,4,7)

#BOOL FONSIYONLAR
#Cogu zaman bir karar verirken dogru yada yanlis oldugunu bilmemiz gerekir
#Iste bize bu durum ici dogru mu yoksa yanlis mi sonucunu veren fonksiyonlar tnaimlariz
#Bu tür fonksiyonlara bool fonksiyonöar denor
#True ya da False döner

#Sayi tek mi cift mi ->x%2==0:cift
#Cift mi fonksiyonu
def cift_mi(x):
    return x%2==0

def tek_mi(x):
    return x%2==1

print(tek_mi(5))





