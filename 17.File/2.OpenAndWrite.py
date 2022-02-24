"""
Read-Write
Okuma Methodlari
read()-->tüm dosyayi tek seferde oku
readline()-->sadece tek satir okur,bir alt satira gecer,bekler
readlines()-->kalan tüm satirlari okur
"""
#with open("kelimeler.txt",mode="rt",encoding="utf-8")as kelimeler_file:
#    text=kelimeler_file.read()
#    print(text)
"""
#Ilk 50 karakter okuyalim
with open("kelimeler.txt",mode="r",encoding="utf-8")as kelime:
    text=kelime.read(50)
    print(text)

#Kelimeler.txt satir satir okuyalim
with open("kelimeler.txt",encoding="utf-8") as only_line:
    line1=only_line.readline()
    line2=only_line.readline()#ctrl+d-->2nci Satir
    print(line1)

with open("kelimeler.txt") as file:
    for satir in file:
        print(satir.split())
"""
#Yazma Islemleri
#w-->write:bos dosya olarak acar(dikkat)
#a-->append:mevcut dosyaya ekleme yapar

#w ile ac
#with open("kelimeler.txt",mode="w") as file:
#    file.write()

#a ile ac
with open("kelimeler.txt",mode="a") as file:
    file.write("\nHello World1")

#tek seferde birden fazla satir ekle
with open("kelimeler.txt",mode="a") as file:
    added_line=["\nEk Satir1","\nEk Satir2","\nEk Satir3","\nEk Satir4"]
    file.writelines(added_line)











