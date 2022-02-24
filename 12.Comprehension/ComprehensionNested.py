#2 listeyi birlestirip tuple olarak yeni bir lsite olusturalim
harfler=["A","B"]
sayilar=[1,2,3]

sonuc=[]
for harf in harfler:
    for sayi in sayilar:
        tup=(harf,sayi)
        sonuc.append(tup)
print(sonuc)

sonuc1=[(harf1,sayi1)
        for harf1 in harfler
        for sayi1 in sayilar
]
print(sonuc1)

#1'den 10 kadar olan tüm sayilari kendileri key kendinden kücük pozitif tamsayilar value listesi olacak sekilde bir dict
sozluk1={}

for e in range(1,11):
    for j in range(1,e+1):
        if not e in sozluk1:
            sozluk1[e]=[j]
        else:
            sozluk1[e].append(j)

print(sozluk1)
