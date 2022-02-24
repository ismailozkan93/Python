#20 den büyük karakterli satirlari aliniz
file=open("metin.txt")
for index,line in enumerate(file):
    if(len(line)>25):
        print(index,line)

print("********************")
#Icinde sesli harf bulunmayan tüm kelimeleri bize versin
file=open("metin.txt")
for line in file:
    #if not ("e" in line and "a" in line and "d" and "t" and "g"):
    if("ipsum" in line):
        print(line)

#file=open("metin.txt")
def yasak_harf_var_mi(metin,yasak_harf):

    for harf in metin:
        if harf in yasak_harf:
            print("Yasak harf vardir")
            return True
    else:
        print("Yasak harf yoktur")
        return False

#yasak_harf_var_mi("Yarin okul vaer mi","tü")

def sadece_sunlari_kullanin(metin,harfler):

    for harf in metin:
        if not harf in harfler:
           print("Baska harflerden olusmaktadir")
           return False
    else:
        print("Metin bu harflerden olusmaktadir")
        return True
#sadece_sunlari_kullanin("Ankara bak","Ankar b")

##2nci yol
"""
def sadece_sunlari_kullan(metin,harfler):
    for harf in metin:
        #harf gercekten harf mi,yoksa noktalama isaretimi?-> isalpha()
        if harf.isalpha() and not harf in harfler:
            return False
    else:
        return True
"""


def lorem_sadece_sunlar():
    file = open("metin.txt")
    for line in file:
        if sadece_sunlari_kullanin(line,"rem"):
            print(line)

lorem_sadece_sunlar()
