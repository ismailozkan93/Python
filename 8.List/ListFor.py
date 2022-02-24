peynirler=["Ezine","Hellim","Tulum"]
print(peynirler)

for peynir in peynirler:
    print(peynir)

for index,i in enumerate(peynirler):
    print(index,i)

sayilar=[1,3,5,7]

for sayi in sayilar:
    sayi=sayi*10
    print(sayi)

for index,sayi in enumerate(sayilar):
    sayi=sayi*10
    sayilar[index]=sayi

print(sayilar)

for index,peynir in enumerate(peynirler):
    peynir=peynir+ " peyniri"
    peynirler[index]=peynir

print(peynirler)