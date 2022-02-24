def harf_say(metin):
    harfler=dict()

    for harf in metin:
        if harf.isalpha():
            if harf in harfler.keys():#harf harfler sözlügünde var mi
               harfler[harf] =harfler[harf]+1
            else:
                harfler[harf]=1
    print(harfler)
    return harfler

def harf_listele(metin):
    sozluk=harf_say(metin)#metini verdik dict olarak aldik

    harfler=dict()  #harfler={}
    for key in sozluk:
        deger=sozluk[key]

        #bu deger daha önceden harfler'e eklenmis mi?

        if deger not in harfler:
            #yoksa ekle
            harfler[deger]=[key]
            #varsa listeye append et
        else:
            harfler[deger].append(key)
    print(harfler)
    return harfler

harf_listele("Ankara nin tasina bak")
#list dict:value olabilirler ama KEY OLAMAZLAR

#Daha önce,Dictionary nin hashtable yapisini kullandigini söylemistik.Key'ler **HASHABLE**  olmalidir
a=[1,2]
s=dict()
#s[a]="hooop"--->TypeError: unhashable type: 'list'
print(s)

##HASH:herhangi türde bir eger alip int dönen foksiyondur, bir nevi INDEX'tir

##MUTABLE olanlar HASHLANAMAZ

#dICTIONARY,LIST,SET IMMUTABLE'DIR VE dict key olamazlar
#Key olabilcekler:int,float,bool,ster,tupple,frozenset

















