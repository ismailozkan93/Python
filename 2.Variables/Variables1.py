#Python Veri Tipleri
# Text(Metin) Tipi:***str***
# Numeric Tipler:**int,float**
# Liste Tipleri:**list,tuple,range**
# Iliski Tipi:**dict**
# Küme Tipi:**set**
# Boolean Tipi:**bool**
#Bir degiskenin tipi: type()

text="This is a text"
print(type(text))
num=5

print(type(num))
num1=6.7

print(type(num1))
list=[1,3,5,7,9]

print(list)
print(type(list))

tuple=("A","B","C")
print(type(tuple))

range15=range(15)
print(range15)
print(type(range15))

dictionary={
    "name":"John",
    "surname":"Alberto",
    "Programming":"Python"
}
print(dictionary)
print(type(dictionary))

küme=set([1,2,4,5,7,5,5,3,4])
print(küme)
print(type(küme))

dogru=True
yanlis=False

print(dogru)
print(yanlis)
print(type(dogru))