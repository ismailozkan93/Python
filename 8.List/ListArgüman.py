#Listin Argüman olarak FOnksyiona Gecilmesi
harfler=["a","b","c"]

print("Fonksyiona gecmeden önce harfler: ",harfler)

def buyuk_harf_ekle(harf_listesi):
    harf_listesi.insert(1,"A")
    harf_listesi.insert(3,"B")
    harf_listesi.insert(5,"C")

buyuk_harf_ekle(harfler)
print("Fonksyiona gectikten sonra harfler: ",harfler)

##Listler,daha dogrusu NON-PRIMITIVELER bir fonksiyona parametere olrak gecince
##kendileri gecer(adresleri gecer)-->Pass By Reference

#Fonksiyon icinde Listeyi Tekrar Atama Örnegi##Degisiklik olmaz
def buyuk_harf_ekle(harf_listesi):
    harf_listesi=["X","Y","Z"]

print("Fonsiyon icinde atama yapildiktan sonra harfler",harfler)
#Non primitivelerde yeniden atamada kopyasini olusturur,adresini degistir orjinal listeye dokunmaz
