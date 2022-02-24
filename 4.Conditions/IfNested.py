#Not Operatörü
#Bir yargiyi (True veya False) cevirmek icin kullanilir,degilse okunabilir
x=4
if not x==5:
    print("x 5'e esit degildir")
else:
    print("x 5 'e esittir")
##IF ler iceri girmek icin TRUE ' ya ihtiyac duyarlar
#**if TRUE:**

x=300
y=3000

if x==y:
    print("x ile y ayni")
else:
    if x>y:
        print("x'y'den büyüktür")
    elif x==y: #redundant kod -->gereksiz kod yazmasakta olur
        print("x ile y ayni")
    else:
        print("x y'den kücüktür")

def sayi_tek_mi():
    sayistr=input("Lütfen sayi giriniz")
    sayi=int(sayistr)
    if(sayi<10):
        if(sayi%2==0):
            print("SAYI 10'dan kücük ve cift")
        elif(sayi%2==1):
            print("SAYI 10'dan kücük ve tek")
    elif(sayi>10):
        if (sayi % 2 == 0):
            print("SAYI 10'dan büyük ve cift")
        elif (sayi % 2 == 1):
            print("SAYI 10'dan büyük ve tek")
    else:
        print("Sayi 10'a esittir")


sayi_tek_mi()