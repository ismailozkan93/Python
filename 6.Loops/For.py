"""
#For Döngüsü
#belirli bir aralikta-->range(baslangic,bitis,artis)
                               #baslangic-->dahil,bitis-->haric
for i in range(10):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(5,31,3):
    print(i)

"""
#Grilen tüm sayinin asal carpanlarini yaziniz
sayi=int(input("Lütfen bir sayi giriniz"))
for i in range(2,sayi+1,1):
    if(sayi%i==0):
        print(i,"sayisi",sayi,"'nin bir carpandir")


#GIRILEN SAYININ ASAL olup olmadigini bulalim
sayi1=int(input("Lütfen bir sayi giriniz"))
asal_mi=True
for i in range(2,sayi):
    if(sayi1%2==0):
        asal_mi=False

if asal_mi:
    print(sayi1,"asal sayidir")
else:
    print(sayi1,"asal degildir")

#Tek for döngüsü icinde 20'den 1 e kadar tek sayilari geriye dogru yazin
#range(baslangic,bitis,-artis)
#for i in range(20,1,-1)

