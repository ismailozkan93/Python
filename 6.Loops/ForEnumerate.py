##Bazen, for döngüsü ile gezerken, döngünün o andaki indeksine ihtiyac duyariz
#Bunun icin hazir bulunan emurate() fonksiyonu kullanilir
#***
metin=input("Lütfen bir metin giriniz")
yen_metin=""
for index,harf in enumerate(metin):
    yen_metin=harf
    #son index geldigimizde "-" karakterini istemiyoruz
    if index<len(metin)-1:
       yen_metin=yen_metin+"-"
    print(yen_metin)

##10'dan baslayip 100'e kadar(dahil) 5'er saydigimizi farzedelim
#Acaba 6. sirada saydigimiz kactir
aralik=range(10,101,5)
for index,sayi in enumerate(aralik):
    if(index==5):
        print(sayi)
        