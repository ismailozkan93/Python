#Dictionary =sözlük yapilari
calisan={
    "ad":"Klar Kent",
    "soyad":45,
    "bölüm":"Haber Servisi"
}
print(calisan)

#Dictionary Bir eslesmedir
#Dictionary'i listin daha genel bir yapisi olarak düsünebiliriz
#Listte indexler tam sayi olmalidr ve python belirler
#Dictionary'de indexleri biz bleirleriz,sadece tam sayi olmak zorunda deilgidr
#{key:value} key-value pair
#key unique'dir

##Dictionary Olusturma
##Listler [] ile dictionary {} ile olusturulur list(),dict()
#Ingilizce-Türkce sözlük
ingTr={}
print(type(ingTr))

araba={
    "Audi":"DEU",
    "Mazda":"JAPAN",
    "FIAT":"ITALY"
}
print(araba)

a=dict()
print(a)
araba2=dict({
    "Audi":"DEU",
    "Mazda":"JAPAN",
    "FIAT":"ITALY"
})
print(araba2)

##Listlere index ile erisilir dic de index yoktur onun yerine key yazilir
print(araba2["Audi"])


