##Simdi bir poligon cizelim

import turtle

def poligon(tospik,mesafe,kenar_sayisi):
    #dönüs derecesi:aci/kenarsayisi
    aci=360/kenar_sayisi
    for i in range(kenar_sayisi):
        tospik.fd(mesafe)
        tospik.lt(aci)

tospik=turtle.Turtle()

poligon(tospik,100,6)
turtle.resetscreen()#ekrani bosalt==turtle.clear()



#Isimlendirilmis parametreler-->keyword arguments
poligon(tospik=tospik,mesafe=100,kenar_sayisi=8)
turtle.mainloop()