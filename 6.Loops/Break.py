#Döngüden cikis_:BREAK
#bAZEN BIR DÖNGÜ tamamlanmadan cikmamiz gerekebilir
#Bunun icin "break" keyword kullanilir

metin=input("Lütfen bir metin giriniz: ")
for i in metin:
    #bosluk mu diye kontrol
    if i==" ":
        break
    print(i)


##30'dan 100 e kadar olan sayilari yazalim
##Eger yazdgimiz sayi 11in kati ise yazip sonra döngüden cikalim
aralik=range(30,100)
for i in aralik:
    if(i%11==0):
        print(i)
        break
    print("**",i)