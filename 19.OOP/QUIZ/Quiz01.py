"""
Adı Ogrenci olan bir class tanımlayın.
Ogrenci'nin 2 özelliği var:
* isim (str)
* numara (str)
Bu Ogrenci class'ından iki öğrenci yaratın.
Bilgileri şu şekilde olacak:
1- isim: James Bond, numara: 007
2- isim: Klark Kent, numara: 333
Sonra bu iki öğrencinin adlarını print edin.
"""
class Ogrenci:
    def __init__(self,isim,numara):
        self.isim=isim
        self.numara=numara


ogr1=Ogrenci("James Bond","007")
ogr2=Ogrenci("Klark Kent","333")
print(ogr1.isim)
print(ogr2.isim)

# Soru 2:
"""
Soru 1'deki Ogrenci class'ımızın şimdi de kayıt olduğu dersleri tutan,
bir attribute'u (özelliği) daha olsun. 
Bu özelliğin adı 'dersler' olsun ve list tipinde olsun.
Bu özellik, Ogrenci yaratılırken boş liste olarak initialize olacak.

Ogrenci derslere birer birer katılacak.
Dolayısı ile 'derse_katil()' adında bir metodu da olacak.
Be metod parametre olarak katılacak dersi alacak.
Eğer ders henüz listede yoksa, o zaman kayıt olacak.

Ek olarak 'get_dersler' adında bir metod daha olacak.
Bu metod bize öğrencinin kayıt olduğu ders listesini verecek.

Buna göre Ogrenci class'ını modifiye edin.

Öğrencinin bilgileri şu şekilde olacak:
isim: Cin Ali, numara: 1111
katılacağı dersler: Temel Python ve Yapay Zeka

Beklenen Sonuç:
ogrenci.get_dersler()  ->  ['Temel Python', 'Yapay Zeka']
"""
class Ogrenci1:

    def __init__(self,isim,numara):
        self.isim=isim
        self.numara=numara
        self.dersler=[]
    def derseKatil(self,ders):
        #Bu ders yoksa ekleyecek
        if not ders in self.dersler:
            self.dersler.append(ders)
    def getDersler(self):
        return self.dersler

ogr11=Ogrenci1("james bond","007")
ogr11.derseKatil("Python")
ogr11.derseKatil("Yapay Zeka")

print(ogr11.getDersler())


"""
İsmi Point olan bir class tanımlayın. 
X-Y koordinat düzleminde bir noktayı temsil etsin.
Docstring'i şu olsun: "(x,y) koordinat düzlemindeki bir noktayı gösterir."
Point'in iki attribute'u vardır: 
    * x (int) 
    * y (int)
Point'in __init__() metodunu tanımlayın.
Ek olarak uzaklık hesaplayan bir metodu vardır. Adı 'uzaklik'.
'uzaklik' metodu parametre olarak ikinci bir Point alır.
Ve kendisi (self) ile ikinci nokta arasındaki mesafeyi hesaplayarak döner.

İpuçları:
* uzaklık şöyle hesaplanır:
    * x'ler arasındaki farkın karesi ile 
    * y'ler arasındaki farkın karesinin toplamının karekökü
    * d = math.sqrt(x_ler_farki**2 + y_ler_farki**2)
Örnek çağırma:
nokta_1 -> (1, 7)
nokta_2 -> (4, 3)
uzaklik = nokta_1.uzaklik(nokta_2)
print(uzaklik)

Beklenen Cevap: 5.0
"""
import math
class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    def uzaklik(self,diger):
        x_ler_fark=self.x-diger.x
        y_ler_fark=self.y-diger.y
        d=math.sqrt(x_ler_fark**2+y_ler_fark**2)
        return d

nokta_1=Point(1,7)
nokta_2=Point(4,3)
print(nokta_1.uzaklik(nokta_2))


class Rectangle:
    def __init__(self,p1,p2,p3,p4):
        self.kose1=p1
        self.kose2=p2
        self.kose3=p3
        self.kose4=p4
        self.en_hesapla()
        self.boy_hesapla()
    def en_hesapla(self):
        self.en=self.kose1.uzaklik(self.kose2)
    def boy_hesapla(self):
        self.boy=self.kose1.uzaklik(self.kose3)

    def alan(self):
        return self.en * self.boy

p1=Point(5,8)
p2=Point(9,8)
p3=Point(5,2)
p4=Point(9,2)

rect=Rectangle(p1,p2,p3,p4)
print(rect.en)
print(rect.boy)
print(rect.alan())


















