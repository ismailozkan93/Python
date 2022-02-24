#Bu modul,kullanicidan bir girdi ister
#Istenen sonuct tipi ne ise ona göre sonuc döner

def girdi_iste(tip="metin"):
    return input("Lütfen bir {0} giriniz".format(tip))

def string_al():
    girdi=girdi_iste()

def tamsayi_al():
    while True:
        try:
            girdi=girdi_iste(tip="tamsayi")
            sayi=int(girdi)
        except ValueError:
            continue
        else:
            return sayi


def ondalik_say_al():
    while True:
        try:
            girdi = girdi_iste(tip="ondalik")
            ondalik_sayi = float(girdi)
        except ValueError:
            continue
        else:
            return sayi