import turtle

def poligon(tospik,mesafe,kenar_sayisi):
    #dönüs derecesi:aci/kenarsayisi
    aci=360/kenar_sayisi
    for i in range(kenar_sayisi):
        tospik.fd(mesafe)
        tospik.lt(aci)

tospik=turtle.Turtle()

#Bir cember cizen fonksiyon yazalim
#50 kenarli bir poligon cizelim

import math
def cember(t,r):
    cevre=2*math.pi*r
    kenar_sayisi=50
    mesafe=cevre/50
    poligon(t,mesafe,kenar_sayisi)

cember(tospik,100)
turtle.mainloop()
