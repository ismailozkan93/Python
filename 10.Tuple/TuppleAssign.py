#Tuple Atamasi
a=99
b=1
#a nin degeri b'ye, bnin degerini de a 'ya atamak istiyoruz
#karsilikli atama

#Yöntem 1->Gecici degisken
print("a:",a)
print("b",b)
gecici=a
a=b
b=gecici
print("a:",a)
print("b:",b)
##Python'da Tuple Atamasi bu islemi(SWAP) otomatik yapar
a=99
b=1
print("a:",a)
print("b",b)
a,b=b,a
print("a:",a)
print("b:",b)

##TUPLE ATAMASI icin iki tarafin degisken sayisi ayni olmalidir
a,b=500,800
print("a:",a)
print("b:",b)
a,b=400,1000
print("a:",a)
print("b:",b)
#a,b=500,1200,40## to many values error

##Alistirma
#Tuple atamasi ile email icindeki kullanici adi ve domain adini ayiralim
#admin@gmail.com
a="admin@gmail.com"
b=a.split("@")
print(b)
kullanici_adi,domain=a.split("@")
print(kullanici_adi)
print(domain)
#Bir liste icindeki her bir degeri ayri bir degiskene atayalim

a,b,c,d=["Python","Java","JavaScript","C#"]
print(a,b,c,d)
















