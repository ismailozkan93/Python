#Fonksiyon tanimlamak
#tanimlamak:definition
#Parametresiz fonksiyon tanimlamak
def fonksiyon_adi():
    print("first function")

#fonksiyon cagirmak
fonksiyon_adi()

#indent:Python'da indent yapisi ile kod bölümlendirilir
#indent==tab veya indent==4 space

#Parametresiz fonksiyon

def ogrenci_adi():
    print("John Doe")

def ogrenci_yasi():
    print(24)

def ogrenci_dili():
    print("Python")

ogrenci_adi()
ogrenci_yasi()
ogrenci_dili()

def ogrenci_bilgileri():
    ogrenci_adi()
    ogrenci_yasi()
    ogrenci_dili()

ogrenci_bilgileri()


print(type(ogrenci_bilgileri))

#Adi ve soyadini ayri yazdirmak istersek
def ogrenci_ilk_adi():
    print("Adi:Peter")
def ogrenci_soyadi():
    print("Soyad:Parker")
def ogrenci_adi():
    ogrenci_ilk_adi()
    ogrenci_soyadi()

ogrenci_adi()
print("*************")
ogrenci_bilgileri()

#Isleme sirasi(Execution Flow) ilk satirdan itibaren calismaya baslar
#Ve asagi dogru iner.

