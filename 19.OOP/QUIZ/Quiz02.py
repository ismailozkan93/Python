"""
Adı BankaHesabi olan bir class tanımlayın.
BankaHesabi'nin bir attibute'u vardır: bakiye (int)
Ek olarak iki adet metodu vardır:
* para_cek(tutar)   -> hesaptan para çeker
* para_yatir(tutar) -> hesaba para yatırır

İki metod da bakiye'yi günceller ve ikisi de geriye, kalan bakiye'yi döner.
Hesap açılırken (__init__) bakiye değeri 0'dır.
Ek olarak her seferinde print() yazmamak için, class içerisinde 'bakiye_goruntule' diye
bir metod olsun.
Bu metod çağrılınca şöyle yazsın: Hesap bakiyesi: xxxxxx

Örnek Çağırma:
hesap = BankaHesabi()
hesap.bakiye_goruntule()
hesap.para_yatir(500)
hesap.bakiye_goruntule()
hesap.para_cek(200)
hesap.bakiye_goruntule()

Beklenen Sonuç:
Hesap bakiyesi: 0
Hesap bakiyesi: 500
Hesap bakiyesi: 300
"""
class BankaHesabi:


    def __init__(self):
        print("Welcome")
        self.bakiye = 0

    def para_goruntule(self):
        print("Bakiyeniz:{0}".format(self.bakiye))

    def para_cek(self,tutar):
        self.bakiye -= tutar
        return self.bakiye

    def para_yatir(self,tutar):
        self.bakiye +=tutar
        return self.bakiye

hesap=BankaHesabi()
hesap.para_goruntule()
#hesap.para_yatir(2000)
hesap.para_goruntule()
print(hesap.bakiye)


class MinumumBakiyeHesabi(BankaHesabi):
    def __init__(self,minumum_bakiye):
        super().__init__()  #elimizde bir bakiye olusur
        self.minimum_bakiye=minumum_bakiye

    #Paracek metodunu overrride etmemiz lazim
    def para_cek(self,tutar):
        if self.bakiye-tutar<self.minimum_bakiye:
            print("Üzgünüz, çekilmek istenen tutar minimum_bakiye'nin altında.")
        else:
            BankaHesabi.para_cek(self,tutar)

    #__str__() overload edicez

    def __str__(self):
        return "Bu minumum bakiye sinifidir"

min_hesap=MinumumBakiyeHesabi(400)
print(min_hesap)
min_hesap.para_yatir(500)
min_hesap.para_goruntule()
min_hesap.para_cek(60)
min_hesap.para_goruntule()

# Soru 7:
"""
Aşağıdaki print() fonksiyonları ekrana ne yazar?

class K:
    def a(self):
        return self.b()

    def b(self):
        return 'K'

class L(K):
    def b(self):
        return 'L'

k = K()
l = L()
print(k.a(), l.a())
print(k.b(), l.b())
"""
#Aşağıdaki print() fonksiyonları ekrana ne yazar?

class K:
    def a(self):
        return self.b()

    def b(self):
        return 'K'

class L(K):
    def b(self):#Önce kendisinde gösterir
        return 'L'

k = K()
l = L()
print(k.a(), l.a())
print(k.b(), l.b())























