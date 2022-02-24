#Pythondaki Anahtar kelimeler (KEYWORD paketi icinde yer alir)

#import Paketimizi iceri alir
import keyword
#1)simdi keyword listesini alalim 2)Bu listeye bir degisiklik atayalim

anahtar_kelimeler=keyword.kwlist

#Simdi bu listeyi yazdir
print(anahtar_kelimeler)

#iskeyword ile keyword olup olmadigi anlasilir
print(keyword.iskeyword("not"));
print(keyword.iskeyword("a"));
x=y=z="Portakal"
print(x)
print(y)
print(z)
