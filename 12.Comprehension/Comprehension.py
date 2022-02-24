#Comprehension -->Python dizi tipinde degiskenler üzerinde kolayca döngü kurmmaizi saglayan yapilardir
kareler=[]
for i in range(1,11):
    kareler.append(i**2)

print(kareler)

#Comprehension
kareler_comp=[i**2 for i in range(1,11)]
print(kareler_comp)

#1 den 7 ye olan sayilarin kupleri
kupler=[]
for i in range(1,7):
    kupler.append(i**3)

print(kupler)
kupler_comp=[i**3
             for i in range(1,7)]
print(kupler_comp)

text="lorem ipsum"
buyuk=[]
for t in text:
    buyuk.append(t.upper())
print(buyuk)


buyuk_comp=[t.upper()
            for t in text]
print(buyuk_comp)
diller=["Python","Java","JavaScript","C#"]
yillar=[1995,1989,1997,2000]
sozluk=dict()
dictionary=zip(diller,yillar)
for a,b in dictionary:
    sozluk[a]=b
print(sozluk)

sozluk_comp={a:b
            for a,b in zip(diller,yillar)}
print(sozluk_comp)

papatya="papatya"
#comprehension
harfler=set()
harfler={harf for harf in papatya}
print(harfler)
