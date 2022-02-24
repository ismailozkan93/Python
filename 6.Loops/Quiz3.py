def uc_bes():
    for i in range(1,51,1):
        if (i % 3 == 0 and i % 5 == 0):
            print("ÜCBEJ")
        elif(i%3==0):
            print("ÜJ")
        elif(i%3==0):
            print("BEJ")
        else:
            print(i)

#uc_bes()

#split() bsluk karakterinden keser
metin=input("Lütfen cümle giriniz")
metin_split=metin.split()

def kelime_birlestir(metin):
        birlesmis_cumle = ""
        for index,kelime in enumerate(metin_split):

            #print(kelime)
            birlesmis_kelime=""
            for harf_index,harf in enumerate(kelime):
                #print(harf)
                birlesmis_kelime += harf
                if(harf_index<len(kelime)-1):
                    birlesmis_kelime +="-"
            print(birlesmis_kelime)
            birlesmis_cumle +=birlesmis_kelime+"__"
        print(birlesmis_cumle)


kelime_birlestir(metin)