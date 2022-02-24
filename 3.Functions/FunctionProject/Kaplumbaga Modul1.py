#Turtle modülünü iceri alalim
import turtle
tospik=turtle.Turtle()
#kaplumbaga ekranda kalir
turtle.mainloop()
#Kaplumbaga olusturan fonksiyon

import turtle
def kaplumbaga_yarat():

    tospik=turtle.Turtle()##turtle nesnesi olustur
    print(tospik)
    return tospik

tospik=kaplumbaga_yarat()
#turtle.mainloop()#kullanicinin ekrani kapatana kadar  beklmesini söyler YAZMASAK ISLEM KAPANIR

#METOD==FONKSIYON
#turtle.fd(n) n pixel ileri
#turtle.bk(n) n pixel kadar geri
#turtle.lt(d) d acisi kadar sola dön
#turtle.rd(d) d acisi kadar saga dön

#tospik.fd(200)
#tospik.lt(90)
#tospik.fd(100)


#Kare cizelim
tospik.fd(100)
tospik.lt(90)
tospik.fd(100)
tospik.lt(90)
tospik.fd(100)
tospik.lt(90)
tospik.fd(100)
turtle.mainloop()

#Yukaridaki islemi döngü yardimiyla kolayca yapabiliriz
for i in range(4):
    tospik.fd(100)
    tospik.lt(90)
turtle.mainloop()

