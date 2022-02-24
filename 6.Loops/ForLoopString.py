metin="Python"
for harf in metin:
    print(harf)

#Girilen bir metnin harflerinden sonra "-" karekteri koyalim
metin=input("Lütfen bir metin giriniz")
yen_metin=""
for harf in metin:
    yen_metin=harf+"-"
    print(yen_metin)

###LEN KAVRAMI
#Python'da yapi itibari ile dizi oan tipler(str,list...)icin uzunluk len() fonksiyonu ile bulunur
print(len("Python"))

dizi=[1,"a",5,6,"b"]

print(len(dizi))
