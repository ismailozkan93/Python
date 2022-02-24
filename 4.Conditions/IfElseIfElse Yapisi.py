#Kullanicidan bir sayi isteelim
#Bu sayinin negatif.pozitif,nötr olma durumunu kontrol ettik

def pozitif_mi():
    girdi=input("Bir sayi giriniz")
    # bilgi str olarak gelir onu inte ceviririz
    n=int(girdi)

    if(n>0):
        print("{} sayisi pozitif'dir".format(n))
    elif(n<0):
        print("{} sayisi negatif'dir".format(n))
    else:
        print("{} sayisi nötrdür".format(n))

#pozitif_mi()

##Simdi kullanicidan 1-7 arasinda bir sayi isteyen fonksiyon yazalim
#Fonksyionumuz, bu sayiya göre haftanin hangi günü olduguna göre karar verip, kullaniciya dönsün

def gün_belirle():
    girdistr=input("Lütfen 1-7 arasinda sayi giriniz")
    girdi=int(girdistr)
    if(girdi==1):
        return "Monday"
    elif (girdi == 2):
        return "Tuesday"
    elif (girdi == 3):
        return "Wednesday"
    elif (girdi == 4):
        return "Thursday"
    elif (girdi == 5):
        return "Friday"
    elif (girdi == 6):
        return "Saturday"
    elif (girdi == 7):
        return "Sunday"
    else:
        return "Invalid number"

#print(gün_belirle())


def gün_hafta():
    günnumara=input("Lütfen 1-7 arasinda sayi giriniz")
    #KONTROL 1: TAMSAYI KONTROLÜ
    if günnumara.isdigit():
        girdi = int(günnumara)
    else:
        print("Lütfen tam sayi giriniz")
        return
    print("1.Kontrol basarili")

    #KONTROL 2:SAYININ 1-7 ARASINDA OLMA KONTROLÜ
    if(girdi<1 or girdi>7):
        print("2NCI Kontrol basarisiz")
        print("Lütfen 1-7 arasinda bir sayi giriniz")
        return
    print("2.Kontrol basarili")
    gün_adi=""
    if(girdi==1):
        gün_adi="Monday"
    elif (girdi == 2):
        gün_adi="Tuesday"
    elif (girdi == 3):
        gün_adi="Wednesday"
    elif (girdi == 4):
        gün_adi="Thursday"
    elif (girdi == 5):
        gün_adi="Friday"
    elif (girdi == 6):
        gün_adi="Saturday"
    elif (girdi == 7):
        gün_adi="Sunday"
    else:
        gün_adi="Invalid Value"

    return print(gün_adi)


gün_hafta()