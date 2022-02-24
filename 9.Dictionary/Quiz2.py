def arac_create1():
    arac={}
    arac["marka"]="Ford"
    arac['model']='Mustang'
    arac["yil"]=1964
    arac["renk"]="kirmizi"
    arac["fiyat"]=30000
    arac["km"]=89000
    arac["motor"]=1.6
    return arac
print(arac_create1())


def arac_create2():
    arac=dict()
    arac ["marka"] = "Ford"
    arac ['model'] = 'Mustang'
    arac ["yil"] = 1964
    arac ["renk"] = "kirmizi"
    arac ["fiyat"] = 30000
    arac ["km"] = 89000
    arac ["motor"] = 1.6
    return arac

print(arac_create2())

def arac_create3():
    arac=dict()
    updated={'marka': 'Ford','model': 'Mustang','yil': 1964,'renk': 'Kırmızı','fiyat': 30000,'km': 89000,'motor': 1.6}
    arac.update(updated)
    return arac

print(arac_create3())

def arac_create4():
    arac=dict({'marka': 'Ford','model': 'Mustang','yil': 1964,'renk': 'Kırmızı','fiyat': 30000,'km': 89000,'motor': 1.6})
    return arac

print(arac_create4())

def yeni_arac():
    sozluk=arac_create3()
    yeni_sozluk=sozluk.copy()   #direk olarak sözlügü kopyalar
    sozluk2=dict()
    for item in sozluk.items():
        key = item[0]
        value = item[1]   #key=item[0] value=item[1]
        key=key+"_2"
        yeni_sozluk[key]=value
    return yeni_sozluk

print(yeni_arac())

#Soru5 3 sözlügü birlestir
d1={4:120, 7:60}
d2={'A': 300, 'B':400}
d3={True: 'Doğru', False: 'Yanlış'}
def sozlugu_birlestir(d1,d2,d3):
    sozluk=dict()
    for e in (d1,d2,d3):
        sozluk.update(e)

    return sozluk

print(sozlugu_birlestir(d1,d2,d3))


























"""
{'marka': 'Ford',
 'model': 'Mustang',
 'yil': 1964,
 'renk': 'Kırmızı',
 'fiyat': 30000,
 'km': 89000,
 'motor': 1.6}
"""