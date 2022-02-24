#Döngü:Belirli kurala göre belirlenmis raliklar icinde,belirli bir operasyonu tekrar eden yapidir
#Python'da döngüler WHILE VE FOR anahtar kelimeler olusturur
#While döngüsü
#10'dan baslayip 1'e kadar yazdirmak istiyrouz

n=10
print("Döngüden önce\n",n)
while n>10:
    print(n)
    n=n-1

print("\nDöngüden sonra ",n)

#1'den' 20ye kadar olan tek sayilarin karelerini bulalim:
n=1
while n<20:
    if(n%2==1):
        print("{0}'in karesi {1}".format(n,n**2))
    n=n+1

#1'den 10'a ladar olan cift sayilarinin toplamini bulalm
k=1
toplam=0

while k<11:
   #cift mi
   if k%2==0:
        toplam +=k
   k+=1
print(toplam)

#Girilen bir sayinin tüm carpanlarini blunuz
sayi=int(input("Bir sayi giriniz"))
i=2

while sayi>i:
    if sayi%i==0:
        print(i)
        #print("{0} sayisi {1} sayisinin bir carpanidir",format(i,sayi))
    i+=1

    #Girilen bir sayinin asal olup olmadigini kontrol ediniz

sayi1=int(input("Bir sayi giriniz"))
i=2
asal_mi=True
while sayi>i:
    if(sayi1%i==0):
        asal_mi=False
    i+=1
if asal_mi:
    print("{0} Asal sayidir".format(sayi1))
else:
    print("{0} Asal sayi degildir".format(sayi1))

