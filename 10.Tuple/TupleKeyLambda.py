#key olarak Lambda FOnksiyonu
#Bazen hazir Python fonksiyonlari islemlerini yapabilmek icin sizden bir fonksiyon ister
            #Yani parametre olarak fonksiyon isterler

#Daha önce lambda fonksiyonlari görmüstük
#sort() ve sorted() fonksiyonlari
#Bu fonksiyonlar söyle calisir
#sorted()--->list.sorted(iterable,key=myFunc,reverse=True|False)

arabalar=("Mercedes","Audi","BMW","Porsche","VW")
print(arabalar)
#harf uzunluklarina göre kücükten-->büyüge siralama
def myFunc(e):
    return len(e)

print(myFunc("Audi"))
#sorted() yeni bir fonksiyon olusturur
#key ne yapacigimizi söyler
sorted_arabalar=sorted(arabalar,key=myFunc)
print(sorted_arabalar)

##sort() listeyi yerinde degistirir
#print(arabalar.sort(key=myFunc()))#AttributeError: 'tuple' object has no attribute 'sort'
                        #arabalar tupple'dir--sorted() tuple listeye cevirir islem yapar
                                            #sort() cevirmez islem yapmaz

arabalar_list=list(arabalar)
print(arabalar_list)
arabalar_list.sort(key=myFunc)
print(arabalar_list)
arabalar1=("Mercedes","Fiat","Audi","BMW","Porsche","VW")
##Ayni siralama islemlerini lambda ile yapicaz
#sorted()

arabalar1_list=list(arabalar1)
sort_araba=sorted(arabalar1,key=lambda x: len(x),reverse=False)
print(sort_araba)
sort_araba_list=arabalar1_list.sort(key=lambda x: len(x))
print(sort_araba_list)

#Örnek
harfler=["c","f","b","a","e","d"]
harfler.sort(key=lambda a: a)
print(harfler)
