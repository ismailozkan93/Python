#DICTIONARY VS TUPLE
#Dictionary elemanlari almak icin items() fonksiyonunu kullanir
#Iste bu items() fonksiyonu bize bir Tuple listesi döner
##Dictionary'den--->Tupple a gecis
sozluk={
    "A":ord("A"),
    "B":ord("B"),
    "C":ord("C"),
    "a":ord("a"),
    "b":ord("b"),
    "c":ord("c")
}
print(sozluk)
#items()
print(sozluk.items())

for anahtar,deger in sozluk.items():
    print(anahtar,deger)

#Elemanlar sirali gelmis olabilir ama dictonary'de sirali olmayabilir cünkü index kullanmazlar
#Yukari da dictinary elemanlarini items() ile alinca bize icinde Tuple olan bir list verdi
#Tuple'dan --->>> dictionary'e

aylar_gunler=[("Ocak",31),("Subat",28),("Mart",31),("Nisan",30)]
print(aylar_gunler) ##icinde tuple tutan bir list

aylar=dict(aylar_gunler)
print(aylar)## dictionary oldu

#Zip() ve range foknsiyonu ile haftanin günlerini bir dictionary indexleyelim

aralik=range(1,8)
günler=["Pazartesi","Sali","Carsamba","Persembe","Cuma","Cumartesi","Pazar"]

gunler_hafta=zip(aralik,günler)
print(gunler_hafta)
gunler_dict=dict(gunler_hafta)#zip i Dictionary'e cevirdik -->Zip liste veya dictionary e cevrilir
print(gunler_dict)
#for fermuar in gunler_hafta:
 #   print(fermuar)##list icinde tupple döner

###TUPLE dictionary key yapmak::
##Dictionary Key Immutable olmak zorundadir,Yani Immutable (Degistirilmez) tipler sadece key olabilir
#SIRALI LISTELER
adlar=["Musa","Bruce","Klark","Peter"]
soyadlar=["Arda","Wayne","Kent","Parker"]

#bos dict
ogrenci_durumu={}
dereceler=["AA","DC","FF","FD"]
ogrenci_durumu_list_zip=zip(adlar,soyadlar,dereceler)
for ad,soyad,derece in ogrenci_durumu_list_zip:
    ogrenci_durumu[(ad,soyad)]=derece
    
print(ogrenci_durumu)





























