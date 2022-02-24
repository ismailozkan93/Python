##Dictionary'den Eleman Silme
#List'lerde eleman silmek icin -->pop() ve del()
#Dictionary icin bu methodlar kullanilabilir
ingTR=dict()
ingTR["one"]="Bir"
ingTR["two"]="Iki"
ingTR["three"]="Üc"
ingTR["four"]="Dört"
ingTR["fife"]="Bes"
ingTR["five"]="Bes"
ingTR["six"]="Alti"
ingTR["seven"]="Yedi"
ingTR["eight"]="Eight"
ingTR["nine"]="Dokuz"
ingTR["ten"]="On"
print(ingTR)

ingTR.pop("fife")
print(ingTR)

del ingTR["seven"]
print(ingTR)

del ingTR["ten"]
print(ingTR)