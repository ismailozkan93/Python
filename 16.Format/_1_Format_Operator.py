"""
%Operatoru
%s->string
%d->integer
%f->float
%.<n>f--> sifirdan sonra n hane
"""
import math
gun="Pazartesi"
print("Bugün günlerden %s" %gun)

sayi=28
print("Öklit'e göre %d bir mükemmel sayidir"%sayi)

pi=math.pi
metin="pi sayisi:%.4f"%pi
print(metin)

#Birden fazla % operatoru
bilgi="Python,ilk olarak %d'de yayinlandi ve %.2f yildan fazladir %s süedürüyor"%(1990,3.2,"varligini")
print(bilgi)

#Tuple olrak % operatorü kullanilir
veri=("Peter","Parker",28)
soru= "Selam %s %s,senin yasin, %d, degil mi? "%veri
print(soru)
soru1="Selam %s %s,senin yasin, %d, degil mi? "
print(soru1 % veri)

#Dictionary ile
dosya={
    "path":"./com/pyt",
    "version":1.8,
    "author":"Joker"
}
bilgi="Adres'i %(path)s olan, %(version).1f versiyonlu dosyasi %(author)s yazmistir"%dosya
bilgi1="Adres'i %(path)s olan, %(version).1f versiyonlu dosyasi %(author)s yazmistir"
print(bilgi)
print(bilgi1%dosya)

























