#1)Eger silinecek elemanin indexini biliyorsak->>pop(index)
dizi=["x","y","z","t","E",2,False]

#pop() fonksiyonu bize silinen elemanlari geri döner
deleted=dizi.pop(2)
print(deleted)
print(dizi)
dizi.pop()#sondakini siler
print(dizi)

#2)Eger silinen elemana ihtiyac yoksa:Del
#Dizinin 2.index'teki yani "t" yi silelim dizi=['x', 'y', 't', 'E', 2]
del dizi[2]
print(dizi)
#3Tek seferde birden fazla eleman silmek istiyorsaniz --->slice(dilim)
t=["a","c","d","t","f","A","I",5,False,"Hakim"]
print(t) # index 1 den 5 e kadar sil
del t[1:5]
print(t)
#4)Eger silinecek elemanin kendisini biliyorsak -->INDEX DEGIL--->remove(eleman)
t.remove(5)
print(t)
#t.remove("k") value error verir
