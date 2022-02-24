#soru 1
"""
sayi=int(input("Bir sayi giriniz"))

if(sayi%2==0):
    print("Sayi cift")
else:
    print("sayi tek")
"""

harf=input("harf giriniz")

if(harf=="a" or harf=="e" or harf=="i" or harf=="i" or harf=="o" or harf=="ö" or harf=="u" or harf=="ü"):
    print("Sesli harf:{0}".format(harf))
else:
    print("Sessiz harf:{0}".format(harf))

def hangi_sekil():
    girdi=int(input("Lütfen sayi giriniz"))
    if(girdi==3):
        print("Ücgen")
    elif(girdi==4):
        print("Dörtgen")
    elif(girdi==5):
        print("Besgen")
    elif(girdi==6):
        print("Altigen")
    elif(girdi==7):
        print("Yedigen")
    elif(girdi==8):
        print("Sekizgen")
    elif(girdi==9):
        print("Cokgen")

#hangi_sekil()


#Bir aydaki gün sayısını ekrana yazdırın. Ay'ın adını kullanıcı belirleyecek.

def hangi_meyve():
    ay=input("Ay giriniz")
    gun=int(input("Gün numarasi giriniz"))
    meyve=""
    if(ay=="Ocak" or ay=="Subat"):
        meyve="Portakal"
    elif(ay=="Mart"):
        if(gun<20):
            meyve="Portakal"
        else:
            meyve="Erik"
    elif(ay=="Nisan" or ay=="Mayis"):
        meyve="Erik"
    elif(ay=="Haziran"):
        if (gun < 20):
            meyve = "Erik"
        else:
            meyve = "Karpuz"
    elif (ay == "Temmuz" or ay == "Agustos"):
        meyve = "Karpuz"
    elif (ay == "Eylül"):
        if (gun < 20):
            meyve = "Karpuz"
        else:
            meyve = "Ayva"
    elif (ay == "Ekim" or ay == "Kasim"):
        meyve = "Ayva"
    elif (ay == "Aralik"):
        if (gun < 20):
            meyve = "Ayva"
        else:
            meyve = "Portakal"
    else:
        return "Invalid"
    return print(meyve)

hangi_meyve()