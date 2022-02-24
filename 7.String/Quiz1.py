#Verilen bir metnin tüm kelimelerinin baş harflerini büyük, diğer harflerini ise küçük yapan bir fonksiyon yazın.
#Soru1

def basharf_byk2(metin):
    kck_mtn=metin.lower()
    bas_hrf_byk=kck_mtn.title()
    print(bas_hrf_byk)
    return bas_hrf_byk

#basharf_byk2("kocaMAN bir aILEsi var")

def sadece_bas_harf(metin):
    return metin.lower().title()

#Soru2
metin=input("Bir kelime giriniz")
harf=input("Bir harf giriniz")
def metin_harf_sayi(metin,harf):
    count=metin.count(harf)
    print(count)
    return  count

#metin_harf_sayi(metin,harf)

#Soru her bir harf kac defa geciyor
def harf_kac_kere():
    cümle=input("Lütfen bir cümle giriniz")
    yazilan_harfler=""

    for harf in cümle:
        if(harf==" "):
            continue
        adet=metin_harf_sayi(cümle,harf)
        #Eger önceden yazdirilysa yazdirma
        if not harf in yazilan_harfler:
            print("{0} harfi {1} defa geciyor".format(harf,adet))
            yazilan_harfler += harf
        print(yazilan_harfler)

harf_kac_kere()

