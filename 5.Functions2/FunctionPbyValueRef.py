#PASS BY VALUE PASS BY REFERENCE
#Ana kural
#Eger Immutable bir nesne,fonksiyona parametre olarak gecerse
#****SADECE KOPYASI**** gecer.
##kENDISI oldugu yerde hic degismeden kalir

#MUTABLE-->Pass by Reference
#Eger Mutable bir nesne bir fonksiyona parametre olarak gecerse,***REFERANSI***gecer.Yani,eger fonksyion icinde
# bu degisken degisirse,orijinal degisken degismis olur(DICT,LIST,SET)

dil="Python"
print("Fonksiyona Parametre olarak gecmeden önce:",dil)

def degistir(ad):
    ad="Java"

degistir(dil)
print("Parametre olarak gectikten sonra:",dil)

##Str immitable oldugu icin kendisi degil,kopyasi fonksiyona gecer

sayi=45
print("Fonksiyona Parametre olarak gecmeden önce:",(sayi))

def degistir(sayi):
    sayi=8

degistir(sayi)
print("Parametre olarak gectikten sonra:",sayi) ##pass by value


sayilar=[1,2,3,5,7]
print("Parametre olarak gecmeden önce:",sayilar)
def degistir(dizi):
    dizi[0]="A"
    dizi[3]="b"


print("Parametre olarak gectikten sonra:",sayilar)

#Sayilar list tipinde oldugu icin Listler-->MUTABLE 'dir
#fonksiyon icindeki degisiklik,orjinal listeyi de degistirdi-->Pass by Reference



