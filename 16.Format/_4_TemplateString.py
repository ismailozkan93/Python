"""
4-)Template Strings
*"String" modulu altinda Template class i ile kullanilir
*$ isareti ile degisken yerlestirilir
*
"""

from string import Template
ad="Bruce Wayne"
kahraman="Batman"

sablon=Template("$k'in asil adi $a")
print(sablon.substitute(a=ad,k=kahraman))

sayi1=5
sayi2=8
sonuc=sayi1*sayi2
sablon=Template("$a * $b =$c")
print(sablon.substitute(a=sayi1,b=sayi2,c=sonuc))