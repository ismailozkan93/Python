#Tuple da String ve List gibi DIZI tipinde bir degiskendir
#Tuple'lar herhangi bir türdw deger alabilirler ve tam sayilar ile indexlenir
#Dolayisi ile Listlere cok benzerler
#TUPLE'lar --->>IMMUTABLE-----------LIST'ler-->MUTABLE
#Tuple virgül ile ayrilmis bir listedir
#Virgül ile ayrilmis deger girerrek tuple olusturmak

t="x","y","z","q","p"
print(t)
print(type(t))
t2=(1,2,3,4,5)
print(t2)
print(isinstance(t2,tuple))
tek_tuple=("x")
print(tek_tuple)
print(type(tek_tuple))
#TEK TUPLE SONUNDA VIRGUL ile olusturulur

tek_tuple1=("x",)
print(tek_tuple1)
print(type(tek_tuple1))

#tuple() COnstructor ile tuple olusturmak
t=tuple()
print(isinstance(t,tuple))

#tuple() constructor ile eleman vererek olusturalim
tek=tuple("P")
print(tek)

##**tuple() yapicisi(constructor) icine string, list verirseniz(dizi tipinde) her bir elemanini ayri bir tuple elemani
##haline getirir
dil=tuple("Python")
print(dil)
listem=["A","B","C","D"]
tup_liste=tuple(listem)
print(tup_liste)

#LIST Operasyonlarinin cogu Tuple icin de gecerlidir
#index
tup=("t","u","p","l","e")
print(tup[0])
print(tup[3])

#Index varsa,dilim(slice) da vardir
print(tup[1:4])

#Cümleyi tersten yazdiralim
ay=tuple("Ay, Dünyanin uydusudur")
print(ay[::-1])

##Tuple'lar Immutable(Degistirilemezler)
t=tuple([0,1,2,3,5,5,6,7,8,9])
print(t)
#t[4]=4 degistirilemiyor cünkü immutable
t=tuple([0,1,2,3,4,5,6,7,8,9])
print(t)

#TUPLE KARSILASTIRMA
#Ayni stringlerdeki gibi alfabetik karsilastirir
#1 ve 5 bakti,1 daha önce geldigi icin kücüktür
t=(1,2,3)<(5,4,3)
print(t)
print((6,40,200)<(6,3,5))
#40ile 3 karsilastirir




