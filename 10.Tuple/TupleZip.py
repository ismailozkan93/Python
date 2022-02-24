##Zip() fonksiyonu
##Python'da List ve Tuple tipleri BERABER kullandiklarinda cok isclevsel olurlar.Bunu detayli görmek icin önce zip() fonk inceleyelim
#ZIP() Python'da hazir fonksiyondur
##Iki veya daha fazla Dizi(Index ile erisilebilen tipler-->List,Tuple,String,Range)
#Zip() her bir dizideki karsilikli elemanlari alarak bir tuple olusturur,böylece tuple'lardan olusan bir zip nesnesi döner

metin="xyzt"
liste=[1,2,3,4]

#metin ve listeyi zipleyelim
fermuar=zip(metin,liste)
print(fermuar)  #zip nesnesi iterator döner
for dis in fermuar:
    print(dis)
##Fermuar icindeki her bir eleman tuple'dir
#Her tuple in ilk elemani metin dizisinden, ikinci elemani liste dizisinden
##Böylece elemanlar karsilikli olarak(ayni index teki) birbirine fermuarlandi

#print(fermuar[0])##TypeError: 'zip' object is not subscriptable
#Eger zip nesnesini List olarak almak ve indexlemek istersek --> list()

d1=["A","B","C","D","E"]
d2=[10,20,30]

yeni_fermuar=zip(d1,d2)
print(yeni_fermuar)
#yeni fermuar zipini liste yap
yeni_fermuar_listesi=list(yeni_fermuar)
print(yeni_fermuar_listesi)

##For ile dönerken,tuple alma
#yeni_fermuar_listesi elemanlari tek tek alalim

for d1,d2 in yeni_fermuar_listesi:
    print(d1,d2)

#Verilen iki listedeki karsilikli elemanlari kontrol edelim,esitse yazdiralim
l1=["a","B","C","d","e","F"]
l2=["A","B","c","d","E","F"]

fermuar1=zip(l1,l2)
print(fermuar1)

for l1_eleman,l2_eleman in (fermuar1):
    if(l1_eleman==l2_eleman):
        print(l1_eleman)


















