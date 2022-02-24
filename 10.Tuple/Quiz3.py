tuple_of_tuples = (('a', 12), ('e', 8), ('b', 16), ('c', 22))
def tuple_sirala(tuple):
    return sorted(tuple,key=lambda x: x[1])

print(tuple_sirala(tuple_of_tuples))

#Soru10:
tup = (5, 2, 3, 3, 4, 2, 1, 3, 4, 5, 2, 1, 2)
sayi = 2

def kac_kere_var(tup, sayi):
    if not sayi in tup:
        raise Exception("Sayi bulunamadi")
    else:
        return tup.count(sayi)


print(kac_kere_var(tup,5))
