##Ismi **kare** olan bir fonksiyon yazin
##Bu fonksiyon kaplumbaga tipinde t adinda bir parametre alsin
##Ek olarak kac yürüyecegini de parametre olarak alsin

import turtle

def kare(t,uzunluk):
                     #t tutrtli tipinde nesne
                     #uzunluk:int tipinde yürüme miktari(pixel)
    #döngü ile kare cizdir
    for i in range(4):
        t.fd(uzunluk)
        t.lt(90)
    return t

tospik=turtle.Turtle()




kare(tospik,100)
kare(tospik,200)
for i in range(10):
    kare(tospik,100+i*20)
tospik.clear()
turtle.mainloop()