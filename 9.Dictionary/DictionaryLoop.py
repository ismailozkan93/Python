##Dictionary nin elemanlari üzerinde dönme
arabalar=dict({
    "Audi":"DEU",
    "Mazda":"JAPAN",
    "FIAT":"ITALY"
})
print(arabalar)

#ITEMS(),KEYS(),VALUES()
for araba in arabalar.items():
    print(araba)

#destructuring
for marka,ulke in arabalar.items():
    print(marka,"-",ulke)

def dic_create(metin):
    harfler=dict()

    for harf in metin:
        if harf.isalpha():
            if harf in harfler.keys():#harf harfler sözlügünde var mi
               harfler[harf] =harfler[harf]+1
            else:
                harfler[harf]=1
    print(harfler)
    return harfler
#dic_create("ankara cok soguk")
#2nci yol
def dic_create2(metin):
    harfler=dict()
    for harf in metin:
        if harf.isalpha():
            harfler[harf]=harfler.get(harf,0)+1
    print(harfler)
    return harfler
dic_create2("ankara cok soguk yarin")
