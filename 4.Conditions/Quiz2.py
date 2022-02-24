def tuhaf_sayi():
    sayi=(input("Lütfen pozitif sayi giriniz"))
    if not sayi.isdigit():
        print("LÜtfen sayi giriniz,bu sayi degil")
        return
    sayi=int(sayi)
    if not(sayi>0):
        print("Lütfen pozitif sayi giriniz")
    else:
        if not(sayi%2==0):
            print("{0} TUHAF'TIR".format(sayi))
        else:
            if(sayi<=10 and sayi>0):
                print("{0} TUHAF DEGILDIR".format(sayi))
            elif(sayi<=20 and sayi>=10):
                print("{0} TUHAF".format(sayi))
            else:
                print("{0} TUHAF DEGILDIR".format(sayi))



tuhaf_sayi()
