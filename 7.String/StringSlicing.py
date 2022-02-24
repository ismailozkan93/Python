##Metin Dilimleme(String Slicing)
##Metinden dilim secmek icin INDEX yapisi kullanilir
##Dilimleme:**
##'dizi[baslangic : bitis : artis]'
##baslangic default=0
##bitis default=son index
##artis default= 1
##[baslangic,bitis)

s="Deep Learning"
print(len(s))
print(s[0:6])
print(s[1:8:2]) #1 baslangic indexi,8 bitis indexi dahil degil 2--> ise artis indexi
print(s[5:13])

rakamlar="123456789"


print(rakamlar[0:10:2])
print(rakamlar[::2])
print(rakamlar[1::2])