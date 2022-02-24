#upper()
kelime="bilgisayar"
yeni_kelime=kelime.upper()
print(yeni_kelime)

#lower()
kelime1="BILGISAYAR"
yeni_kelime1=kelime1.lower()
print(yeni_kelime1)

#strip()
tumce="     Havalar yarindan itibaren güzel olacak        "
print(tumce)
yeni_tümce=tumce.strip()#yeni bir degiskene atayinca degisir
print(yeni_tümce.strip())

#lstrip() left soldaki bosluklari siler
#rstrip() right sagdaki bosluklari siler

s="    bu metnin basinda bosluk var"
print(s.lstrip())
t="  bu metnin sonunda bosluk var          "
print(t.rstrip())

#format():Metni degiskenler ile süsler
A="Python"
B="Yapay"
C="Zeka"
print("{0} ile {1} {2}".format(A,B,C))

#**find()**:Metnin icindeki bir karakter ya da metin parcasi olur
#** Bulursa,ilk buldugu indexi döner
    #Bulamazsa -1

kelime2="Pencereler"
index=kelime2.find("e")
print(index)
index=kelime2.find("ce")
print(index)
#Standart olarak find() fonskyionu en bastan yani 0 index'ten aramaya baslar
#find(metin,baslangic)
index=kelime2.find("r",6)
print(index)
#find(metin,baslangic,bitis)
index=kelime2.find("l",2,8)
print(index)
index=kelime2.find("l",2,6)
print(index)

#Capitalize: ilk harfini büyük yapar
film_adi="batman dark knight"
film_adi=film_adi.capitalize()
print(film_adi)

#title():Metnin bütün kelimelerinin ilk harfini büyük yapar
film_adi="batman dark knight"
film_adi=film_adi.title()
print(film_adi)

#isdigit(): Metin tamsayi mi degil mi
girdi="48"
print(girdi.isdigit())
girdi1="-20"
print(girdi1.isdigit())
girdi2="4.2"
print(girdi2.isdigit())

##startswith():Metnin verilen karakter ya da metin parcasi ile baslar mi?
##endswith():Metnin verilen karakter ya da metin parcasi ile biter mi?
gezegen="Nepton".lower()
print(gezegen.startswith("n"))
print(gezegen.startswith("nept"))
print(gezegen.endswith("on"))

#replace():Metnin icindeki bir karakter ya da metin parcasini,baska bir karakter ya da metin parcasi ile degistirir
bilmece="Carsidan aldim bir tane,eve geldim bin tane,pazara gittim on tane"
bilmece=bilmece.replace("tane","dene")
print(bilmece)

txt="Atlar elma yemeyi cok sever"
x=txt.replace("elma","havuc")
print(txt)
print(x)



