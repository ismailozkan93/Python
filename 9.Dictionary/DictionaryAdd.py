##ELEMAN EKLEME
#Listelerde eleman eklemek icin -->append(),insert()
#Dictionary icin bu metodlar yoktur
#dict[key]value

ingTR=dict()
print(ingTR)

ingTR["one"]="Bir"
ingTR["two"]="Iki"
ingTR["three"]="Üc"

print(ingTR)
##append dict icin yoktur
ingTR["four"]="Dört"
ingTR["fife"]="Bes"
print(ingTR)
ingTR["five"]="Bes"
ingTR["six"]="Alltti"
print(ingTR)
ingTR["six"]="Alti"
print(ingTR)
ingTR["seven"]="Yedi"
ingTR["eight"]="Eight"
ingTR["nine"]="Dokuz"
ingTR["ten"]="On"
print(ingTR)

##UPDATE()
arac={
    "marka":"Ford",
    "model":"Mustang",
    "yil":1964
}
print(arac)

#arac sözlügüne renk ekleyelim
eklenecek={"renk":"kirmizi"}

arac.update(eklenecek)
print(arac)
eklenecekler={"fiyat":300000,"km":89000,"motor":1.6}
arac.update(eklenecekler)
print(arac)
















