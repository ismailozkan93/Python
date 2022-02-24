##1.yol
import math


def selamlama(str1,str2):
    print("selam "+str1+" ve "+str2)

str1="Clark Kent"
str2="SpiderMan"
selamlama(str1,str2)

##2.yol---> str format
def isim_selamlama(str1,str2):
    print("Selam {0} ve {1}".format(str1,str2))

isim_selamlama("Bruce Wayne","Batman")

#Soru 3
def ismini_söyle():
    #input tusu enter tusu bekler
    isim=input(" Lütfen isminizi söyler misiniz ")
    #enter sonrasinda kod devam eder
    print("Selam sana {0}".format(isim))
ismini_söyle()
#Soru 4
"""
Parametre olarak 3 sayı alan bir fonksiyon yazın. <br>
Fonksiyon bu sayılardan en büyüğünü size geri dönsün. <br>
Bu fonksiyonun docstring'ini de yazın. 
"""
def en_büyük(sayi1,sayi2,sayi3):
    maximum=max(sayi1,sayi2,sayi3)
    return maximum

print(en_büyük(5,7,10))
print(max.__doc__)
print(en_büyük.__doc__)

#Soru5
#Parametre olarak gelen metni parçalayan küçük harfe çeviren bir fonksiyon yazın. <br>
#parçalamak için: strip()
#küçük harf yapmak için: lower()

    #Strip() bosluk karakterinden parcalar
def parcala_ve_kücült(metin):
    parcali_metin=metin.strip()
    parcali_ve_kücük_metin=parcali_metin.lower()
    return parcali_ve_kücük_metin

metin="PyThon MacHINe LearnINg"
print(parcala_ve_kücült(metin))

#Soru 6
#Parametre olarak iki sayinin toplamini dönen fonksiyon
def toplam_sayi(sayi1,sayi2):
    toplam=sayi1+sayi2
    return toplam

print(toplam_sayi(7,8))

#Soru 7
"""Parametre olarak gelen 3 sayı alan bir fonksiyon yazın. <br>
Fonksiyon bu sayıların ikili farklarını alsın ve bu farklardan en küçüğünü dönsün. <br>
* Fark için mutlak değeri kullanın -> abs  (absolute value)
* Minimum için -> min
"""
def uc_sayi_fark(sayi1,sayi2,sayi3):
    fark1=abs(sayi1-sayi2)
    fark2=abs(sayi3-sayi2)
    fark3=abs(sayi1-sayi3)
    minumum=min(fark1,fark2,fark3)
    return minumum

print(uc_sayi_fark(5,8,20))

#Soru 8
"""
Parametre olarak bir sayı alan bir fonksiyon yazın. <br>
Fonksiyon bu sayının karekökünü dönsün. <br>
* Karekök için -> math.sqrt()
"""
def karekök(sayi):
    kare=math.sqrt(sayi)
    return kare

print(karekök(81))

#Soru 9
"""
Parametre olarak bir sayı alan bir fonksiyon yazın. <br>
Fonksiyon bu sayının logaritmasını dönsün. <br>
* Logaritma için -> math.log()
"""

def logaritma(sayi):
    loga=math.log(sayi)
    return loga

print(logaritma(12))

#Soru 10
"""Parametre olarak 2 sayı alan bir fonksiyon yazın. <br>
Bu sayıları bir dik üçgenin dik kenarları  olarak düşünelim.
Fonksiyon bu üçgenin hipotenüsünü dönsün. <br>
$$ hipo^2 = a^2 + b^2 $$
"""
def dik_ücgen(a,b):
    hipo=math.sqrt((a**2)+(b**2))
    return hipo

print(dik_ücgen(5,12))