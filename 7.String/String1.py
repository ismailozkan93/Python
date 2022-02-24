"""
Stringler bir dizidir
Stringler birer dizidir(SEQUENCE)
Yani iclerinde siralnamis olarak baska degerler tutan yapilardir
Örnegin bir kelime icinde harf tutar
String bir dizidir
"""
#Pythonda dizi tipinde degiskenlerde,index yapisi ile degiskenin elemanlarina erisilir
meyve="portakal"
print(meyve)

#Pythonda indexler sifirdan baslar
harf=meyve[0]
print(harf)

#Stringin uzunlugu len() fonksiyonuyla alinir
print(len(meyve))
print("son harf: ",meyve[7])

#meyve[8] 8nci index olmadigi icin index out of range hatasi alir

x="pYTHON"
y="Machine Learning"

print(len(x),len(y))
print()