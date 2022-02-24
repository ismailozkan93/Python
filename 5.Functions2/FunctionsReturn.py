#Fonskiyonlar cogu zaman islemlerini bitirdikten sonra geriye dönerler
#Fonksiyonu cagiran yer de o degeri alir ve buna göre islemlerini yapar
#Geriye deger dönmeyen fonksyionlara **void** denir

#***ÖNEMLI NOT *** foNKSYION icinde ,RETURN ifadesiden sonra gelen kodlar calistirilmaz.Cünkü RETURN fonksiyondan
#cikis demektir

import math
e=math.exp(1.0)
print(e)

#Örnegin,dairenin alanini hesaplayan bir fonksiyon yazalim ve degerini alip ekrana basalim

def alan(yaricap):
    a=math.pi*yaricap**2
    return a
print(alan(4))

##Yukaridaki alan fonksiyonu icindeki a degiskenine "GECICI DEGISKEN" denir
#Tek amaci hesaplanan alan degeri tutup bunu return'e vermektir
#Bu gecici degiskenleri kullanmayabiliriz(Genelde debug islemi icin önemlidir)

#gecici degisken kullanmadan
def alan(yaricap):
    return math.pi*yaricap**2
print(alan(5))

##ADIM ADIM GELISTIRME, hata ayiklama(debug) icin olmazsa olmaz bir kavramdir
#Eger programin her adimda neyi yaptigini debug edemezseniz, o zaman her seyi dogru yaptigindan emin olamazsaniz


def uzaklik(x1,y1,x2,y2):
    #xler arasindaki fark
    dx=x2-x1
    #y'ler arasindaki fark
    dy=y2-y1

    #<-------DEBUG-------->
    #Daha fazla devam etmeden bunlari dogru hesapladigimizi kontrol edelim
    print("dx:",dx)
    print("dy:",dy)
#uzaklik(1,6,4,10)#Gelistirmeye devam
    kareler_toplam=dx**2+dy**2
    # <-------DEBUG-------->
    print(kareler_toplam)
    return print(math.sqrt(kareler_toplam))

uzaklik(1, 6, 4, 10)

#TDD(Test Driven Development): Her adimi test ederek ilerlemek





