"""
Dosya:File, byte dizidir
Dosya Tipleri:
1-)Binary Tipi--Ypdf,doc,jpg,png
2-)Text Tipi-->txt,xml,html,.py,.java

Encoding:Verinin bir byte yapisidir-->nasil tutuldugu
Iki yayign encoding sekli
1-)ASCII(128 KARAKTER)
2)UNICODE(1.114.112)


"""
"""
#encoding vermeden
file=open("kelimeler.txt")
print(file.read())
file.close()#-->acilmis dosya kapanmalidir
#encoding vererek
print("***************")
file1=open("kelimeler.txt",encoding="utf-8")
print(file1.read())
"""
#Dosya yoksa-->Hata_FileNotFoundError
try:
    file = open("kelimeler.txt", encoding="utf-8")
except:
    print("Dosya Bulunamadi")
else:
    print(file.read())
    file.close()
finally:
    print("Fertig")

###WITH
#CONTEXT MANAGER
#Dosya acma,okuma ve kapatma islemlerini otomatik yapar

with open("kelimeler.txt",encoding="utf-8")as file:
    icerik=file.read()
    print(icerik)

"""Dosya yoksa-->with FileNotFoundError verir
with open("kelimeler.txt",encoding="utf-8")as file:
    icerik=file.read()
    print(icerik)
"""
"""
Dosya Acma Sekilleri(Modlar)
r:okuma(read)
w:yazma(write)
a:ekleme(append)
x:yaratma(create)
t:text dosyasi formatinda
b:binary dosyasi formatinda
+:update modu(read+write)

"""
with open("kelimeler.txt",mode="rb")as file:
    icerik1=file.read()
    print(icerik1)


















