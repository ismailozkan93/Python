#Lamda Fonksiyonu:
#Bazen bir fonksiyonu isim vermden direk kulanmak isteyebiliriz
#Bunun icin "LAMBDA" anahtar kelimesi kullanilir
#***Lambda*** fonksiyonu(lamda expression "tek satir fonksiyonu" olarak da bilinir)

metin="Selam sana kartal göz"
metin_split=metin.split()
print(metin_split)

#Simdi lambda fonksiyon ile split() fonksiyon kullanalim
#def metni_parcala(metin)
# ...........

metni_parcala=lambda x:x.split()

metni_parcala(metin)

#carpma yapan lambda fonksiyonu
multiply=lambda x, y: x*y
print(multiply(4,8))

#Üstel hesap yapan lambda
üstel=lambda x, y: x**y
print(üstel(3,4))