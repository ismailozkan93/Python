#Set'e eleman eklemek
#add()

notlar=set({"A","B","A","C","B","C"})
print(notlar)

dereceler=set({"A","L","T","B","F"})
print(dereceler)

notlar.add("P")
notlar.add("Q")
print(notlar)
#Setten eleman cikarmak
dereceler.remove("B")
print(dereceler)
#for e in notlar:

#for e in dereceler:

#set Alising islemi
#Listere benzer
a=set({2,5,7})
b=a
b.add("Yeni")
print("a:",a)
print("b:",b)

#is identical
print(a is b)
print(a.issubset(b))
print(a.issuperset(b))

a.add("YYY")
print("a:",a)
print("b:",b)

#SETLERE tek seferde UPDATE() ile cok sayida eleman eklemek

meyveler={"elma","armut","portakal"}
daha_cok_meyve=["cilek","muz","portakal"]
meyveler.update(daha_cok_meyve)
print(meyveler)


