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
#dic.items()
#print(ingTR.items())
#print(ingTR.keys())
#print(ingTR.values())

#for key,value in ingTR.items():
    #print("{} keyinde: {} degeri vardir".format(key,value))

arac={'marka': 'Ford',
      'model': 'Mustang',
      'yil': 1964,
      'renk': 'kirmizi',
      'fiyat': 300000,
      'km': 89000,
      'motor': 1.6}

print(arac.get("marka"))
print(arac["marka"])
print(arac.get("km"))
print(arac["km"])
print(len(arac))
#key icinde arar
print("yil" in arac)
#deger icinde arama icin dict.values
print(1.6 in arac.values())











































