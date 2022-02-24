def hata_firlat():
    girdi=input("Lütfen bir sayi giriniz")

    #eger biz bu olasi hatayi düsünmezsek-->crach
    if not girdi.isdigit():
        raise Exception("Sayi girmediniz,Lütfen Sayi giriniz")

    sayi=int(girdi)
    print(sayi)

#hata_firlat()#fonksiyonu cagir
#ValueError:Invalid literal for int() with base 10:"abc"

def tanimli_hata_firlat():
    girdi=input("Bir sayi giriniz")
    if not girdi.isdigit():
        raise ValueError("Sayi girmediniz,Lütfen Sayi giriniz")

    sayi=int(girdi)
    print(sayi)

#tanimli_hata_firlat()

def girdi_dogrula():
    girdi=input("Lütfen bir sayi giriniz:")
    assert int(girdi),ValueError("Sayi girmediniz")
    sayi=int(girdi)
    print(sayi)

#girdi_dogrula()

def bolme(n1,n2):
    assert n2 !=0,"Sifira bölme yapilamaz"
    print(n1/n2)

#hatasiz cagirma
bolme(10,2)

#hatali cagirma
bolme(10,0)
