#Soru1 Tuple lar immutable 'dir, nasil yeni eleman eklenir

def tuple_create():
    sayilar = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    yeni_sayilar=tuple()
    for e in range(11,21):
        yeni_sayilar=sayilar+(e,)
        sayilar=yeni_sayilar
    print(sayilar)
tuple_create()

#Soru2
t = ('Y', 'a', 'p', 'a', 'y', ' ', 'Z', 'e', 'k', 'a')
def tuple_to_string(tuple):
    x="".join(tuple)
    print(x)
    return x

tuple_to_string(t)

#Soru3
a='Guido van Rossum'
def string_to_list_list_to_tuple(str):
    list1=list(str)
    tuple1=tuple(list1)
    print(tuple1)
    return tuple1

string_to_list_list_to_tuple(a)

#Soru4
metin = ('G', 'u', 'i', 'd', 'o', ' ', 'v', 'a', 'n', ' ', 'R', 'o', 's', 's', 'u', 'm')
ind = 4
def kac_kere_geciyor(tuple,index):

    eleman=tuple[index]
    print(tuple.count(eleman))
    return tuple.count(eleman)

kac_kere_geciyor(metin,ind)