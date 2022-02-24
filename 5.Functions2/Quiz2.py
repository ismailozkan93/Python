import math
def n(c):
    ustu = m(c, c)
    print(c, ustu)
    return ustu


def m(x, y):
    x = x + 2
    return x ** y


def p(x, y, z):
    toplam = x + y + z
    kare = n(toplam) ** 2
    return kare


a = 1
b = a + 1
print(p(a, b + 1, a + b))


def aritmetik_ortalama(*args):
    sum=0
    for x in args:
        sum =sum+x
    ort=sum/len(args)
    print(ort)
    return ort

aritmetik_ortalama(2,5,11)

def daire_alan(r):
    return r*r*math.pi

def daire_alan_toplam(r):
    return (r**2)*math.pi*2

def silindir_dikdörtgen_alan(r,h):
    return 2*math.pi*r*h


def silindir_toplam_alan(r,h):
    toplam_alan=(daire_alan_toplam(r))+silindir_dikdörtgen_alan(r,h)
    print(toplam_alan)
    return toplam_alan

silindir_toplam_alan(10,2)