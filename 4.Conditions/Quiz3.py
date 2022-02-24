def geri_cift_say(bitis,deger):

    if deger==bitis :
        print("-------THE END------")
        return
    else:
        print(deger)
        geri_cift_say(bitis,deger-1)

def büyük_kücük():
    sayi1=int(input("1.sayiyi giriniz"))
    sayi2=int(input("2.sayiyi giriniz"))
    if(sayi1>sayi2):
        print("{0} {1} den büyüktür".format(sayi1,sayi2))
        geri_cift_say(sayi2,sayi1)
    elif(sayi1==sayi2):
        print("{0} {1} e esittir".format(sayi1, sayi2))
    else:
        print("{0} {1} den büyüktür".format(sayi2,sayi1))
        geri_cift_say(sayi1,sayi2)

büyük_kücük()




#geri_cift_say()