def girdi_al(text):
    girdi = input(text)
    return girdi


girdi_tam=girdi_al("Lütfen bir tam sayi giriniz")

def tamsayi_mi(girdi):
    girdi.strip()#Olasilik1: Basindaki ve sonundaki bosluklar kaldirilir
    girdi.strip("+-") #Olasilik2: Kullanici sayinin basina veya sonuna +- koymus olabilir
    if girdi.isdigit():
        print(True)
        return True
    else:
        print(False)
        return False

#tamsayi_mi(girdi_tam)


def recursive():
    if not(girdi_tam).isdigit():
        print("Lütfen tekrar tamsayi giriniz")
    else:
        print(girdi_tam)
        return girdi_tam


recursive()