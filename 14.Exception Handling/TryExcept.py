##Try-Except
#try:
    #kodu calistirmaya calisir
    #hata yoksa,try'in sonuna kadar gelir
    #hata varsa, kod try'dan cikar
#except:
    #eger try icinde hata alinmissa,except gelir
    #derleyici hata olan yerden except icine atlar
    #yani hatanin yakalandigi yer except blogudur

def karesini_al():
    girdi=input("Lütfen bir tamsayi giriniz: ")
    sayi=int(girdi)
    print(sayi)

#karesini_al()

def karesini_hesapla_try():
    try:
        girdi=input("Lütfen bir tamsayi giriniz: ")
        sayi=int(girdi)
        print(sayi)
    except:
        print("Sayi girmediniz,Lütfen sayi giriniz")
karesini_hesapla_try()

#kULLANICI SAYI GIRMEDIGINDE TEKRAR SAYI ISTER
def karesini_hesapla_try_again():
    try:
        girdi=input("Lütfen bir tamsayi giriniz: ")
        sayi=int(girdi)
        print(sayi)
    except:
        print("Sayi girmediniz,Lütfen sayi giriniz")
        karesini_hesapla_try_again()

karesini_hesapla_try_again()

#Olmayan bir dosya acmaya calisalim
def dosya_ac(dosya_yolu):
    dosya=open(dosya_yolu)

    for satir in dosya:
        print(satir.split())



def dosya_ac(dosya_yolu):
    try:
        dosya=open(dosya_yolu)
        for satir in dosya:
            print(satir.split())
    except:
        print("Malesef dosya bulunamadi")
yol="dizilerrr.txt"
dosya_ac(yol)

def bolme_try():
    try:
        bolunen=int(input("Bölünen giriniz:..."))
        bolen=int(input("Bölen giriniz..."))

        bolum=bolunen/bolen
        print(bolum)

    except ValueError:
        print("Tamsayi girmediniz....")

    except ZeroDivisionError:
        print("Bölen 0 olmamali....")


bolme_try()













