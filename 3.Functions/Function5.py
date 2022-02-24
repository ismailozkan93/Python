#Scope yasam alani==scope girinti(indent)
#Python da degiskenler tanimladiklari alanda ve o alanin alt alanlarinda gecerlidir

def scope():
    scope_degiskeni=100
    print(scope_degiskeni)

scope()
#print(scope_degiskeni)Degiskene scope disindan ulasilmaya calisilirsa
#PYTHON INTERPRETER hata verir---****NAMEERROR****

#Daha üstte yani **GLOBAL SCOPE** da tanimlanmis bir degiskene erisebilirsiniz

kisa=4
uzun=6
def cevre():
    dikdörtgen_cevre=2*(kisa*uzun)
    print(dikdörtgen_cevre)
cevre()

#Peki GLOBAL SCOPE icindeki bir degiskeni fonksiyon icinden degistirebilir miyiz
def global_change():
    kisa=400 #kisa degiskeni golabaldekinin kopyasidir ve sadece bu scope icinde yasar
    print(kisa)

global_change()

print(kisa)

#Globaldai degisken degistirilcekse degisken basina "GLOBAL" yazilir
def global_change1():
    global kisa
    kisa=400
    print(kisa)
global_change1()
print(kisa)