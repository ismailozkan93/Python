#foNKSIYONLAR 1.SINIF VATANDASTIR
#Fonksiyonlar da degiskenler gibi
#atanabilirler,parametre olarak gecilebilirler,yeniden deger atanabilirler

def kup(num):
    out=num**3
    print(out)
    return out
kup(5)

#foksiyonu bir degiskene atayalim
q=kup
print(type(q))#function

print(q(5))
#q da cagrilinca,birebir kup fonksiyonu ile ayni seyi yapti
#Cunku zaten q,kup fonksiyonu demektir
#Sadece yeni bir ad verdik,buna "ALISING"=="YENIDEN ADLANDIRMA" denir

def selamlama(metin):
    print(metin)
selamlama("Merhaba Python")
hello=selamlama
hello("hi there")

#PARAMETRE SAYISI önceden bilinmiyorsa:*args
#Bazen bir fonksiyonun hangi argumanlari(parametreleri) alacagi önceden bilinmez
#Bu durumda *args seklinde parametre alir

def toplam(*args):
    #print("args",args)
    print(sum(args))
    return sum(args)
toplam(5,8,13,14,53)

def parametreleri_yaz(*args):
    for a in args:
        print(a)

parametreleri_yaz("A","byte",46,True)


