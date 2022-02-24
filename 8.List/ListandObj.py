#Nesneler ve Degerler
a="kivi"
b="kivi"
print(id(a))
print(id(b))
##a==b
##Python'da degiskenler ayni ve  immutable oldugu icin
##iki farkli adres olusturmak yerine , ikisini ayni adrese yolladi
##Artik a ve b farkli degerler aldigina göre, b icin yeni bir adres olusturdu
b="kivis"
print(id(b))

#Eger list degiskenleri birbirine esit
x=[1,2,3]
y=[1,2,3]
print(id(x))
print(id(y))
##== kontrolü -> esitlik-->deger
##id(x)==id(y) kontrolü--> aynilik(identical)-->nesneler--->IS ifadesiyle de yapilabilir

#IS IFADESI
print(x==y) #deger kontrolü
print(id(x)==id(y)) #nesne kontrolü
print(x is y)

s1="bilgisayar"
s2="bilgisayar"
print(s1 is s2)
