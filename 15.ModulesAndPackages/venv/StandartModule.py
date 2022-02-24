#Standart Moduller
#Module Programlama:
"""
1-Kod tekrarini önler
2-Organizasyon(we,db,api...)
3-Bakimini ve Yönetimini
"""
#Modul: .py ile biten Python dosyalarina
#Paket:Bircok modulü iceren Python klasörleridir

#import edilirek kullanilinir

#import math-->bir moduldür
#import random-->bu modül 0 ile 1 arasinda olasilik verir
import random
rasgele_sayi=random.randint(10,50)
print(rasgele_sayi)
liste=[1,2,3,4,5,6,7,8,9]
eleman=random.choice(liste)
print(eleman)
#örneklem almak istiyorsa
örneklem=random.sample(liste,3)
print(örneklem)

#platform modülü
import platform
print("platform",platform)
print("platform türü",platform.platform())
print("platfomr mimarisi:",platform.architecture())
print("makine tipi:",platform.machine())
print("isletim sistemi:",platform.system())

import sys
#path degiskeni
#print("path:",sys.path)

yollar=sys.path #Python un modul ararken kullanidigi yollar
for yol in yollar:
    print(yol)

#bir modül import ederken adini degistirmek isteyebiliriz
#alise

import random as rnd
print(rnd.random())

#bir modulün bir parcasini import etmek
from math import pi
print(pi)

from sys import modules
print("hazir modules",modules)

#hem parcali hem de alise edilmis import
from math import sqrt as karekok
print(karekok(64))

#* ile import önerilmez isim karmasasi olur



















