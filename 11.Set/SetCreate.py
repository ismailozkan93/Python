#Set küme tipi hazir python veri yapisinda vardir
#Setler birden cok degeri tek bir degiskende tutumak icin kullanilir
#Setler sirasiz(unordered) ve indekslenmemis koleksiyonlardir
#Setler 2 sekildedir:
        #süslü parantez ile(ama icinde eleman vererek)
        #set()consructor ile
#Set'in elemanlari tekildir,matematikteki kümeler gibi

#Set olusturma
#Süslü parantez ile
#ama süslü prantez bos olursa--> dictionary olusturur
#süslü parantez icerisinde eleman vermek lazim
kume={}
print(type(kume))

kume1={"at","kedi","köpek","at","tavsan","kedi"}
print(kume1,type(kume1))

##set() constructor iele küme olusturmak
harfler=set({"A","B","C","D","E"})
print(harfler,type(harfler))

metin="Python Veri Yapilari"
print(set(metin))

##ONEMLI:: SETLER sirasiz yapilardir

