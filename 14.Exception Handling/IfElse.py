"""
try:
    ---kod----
except
    ---hata---
else
    ---hatasiz isleme---
"""



#Kod try icinde calisirken,hata alirsa ilgili except bloguna gelir
#Hata almazsa(vdef dosya_ac(dosya_yolu):
# -->ex degisken adi
def dosya_ac_hata(dosya_yolu):
    try:
        dosya=open(dosya_yolu,encoding="utf-8")
    except FileNotFoundError as ex:
        print(ex)
    else:
        print(dosya.read())


yol="dizilerr.txt"
dosya_ac_hata(yol)

#Bazi durumlarda kodun hic birsey yapmadan devam etmesini isteyyebiliriz--->pass

def dosya_ac_hata_pass(dosya_yolu):
    try:
        dosya=open(dosya_yolu,encoding="utf-8")
    except FileNotFoundError as ex:
        pass
    else:
        print(dosya.read())

dosya_ac_hata_pass(yol)