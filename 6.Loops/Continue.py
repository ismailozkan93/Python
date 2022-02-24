##Döngünün bir sonraki adimini atla:continue
#Bazen döngü icinde dönerken,bir kosula göre, o andaki adimi(ITERATION) atlayip bir sonraki adima gecmemiz gerekebilir

#Bunun icin continue anahtar kelimesi kullanilir

for i in range(1,11):
    #sayi tek ise isleme devam etme-->bir sonraki adima gec
    if(i%2==1):
        continue
    print(i)

metin=input("Lütfen bir cümle giriniz")
for i in metin:
    if(i==" "):
        continue
    print(i)