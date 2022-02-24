#Python'da Listler icin hazir(built in) metodlar vardir
#append():Listenin sonuna yeni bir eleman ekler
#insert():Belli bir index ile listeye eleman ekler
#extend():Listeye baska bir liste ekler
#sort():Listeyi belirli bir siraya göre siralar(yerinde yapar)
#sorted():Listeyi siralar ve sirali olarak yeni bir liste verir

harfler=["a","b","c","d","e"]
print(harfler)
harfler.append("f")
harfler.append("x")
harfler.append("t")
print(harfler)

#insert()
#Listeye eleman eklerken sona degil de, belirli bir siraya ekleyelim
#insert(index,eleman)

print("Insert Öncesi Harfler")
harfler.insert(2,"W")
print("Insert Sonrasi Harfler")
print(harfler)

#extend()
#Listeye baska bir liste ekler
sesli_harfler=["a","e","i","u","o"]
noktali_sesliler=["i","ü","ö"]
print(sesli_harfler)
sesli_harfler2=sesli_harfler.extend(noktali_sesliler)
print(sesli_harfler2)

#sort() listeyi yerinde siralar
t = ["d","c","e","b","a"]
t.sort()#sort()-->default (Kücükten Büyüge)
print(t)
#Reverse parametresi ile siralama yönü degistirilebilir
#reverse=True tersten sirala demektir
#reverse=False normal siralar default
t.sort(reverse=True)
print(t)
#sorted() listenin sirali kopyasini verir
a=[4,2,1,6,3]
print(a)
b=sorted(a)
print(a)
print(b)
c=sorted(a,reverse=True)
print(c)

