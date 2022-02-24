#Dictionary'da key ile deger bulmaya calistik
#Tersini yapip deger ile arama yapip key i bulabiliriz
#Ayni degeri göstren birkac fazla anahatar olabilir, ya ILKINI döneriz, ya da tümünü iceren bir liste döneriz
#Malesef, bu tersten arama islemi icin basit bir yöntem yok.Dolayisiyla seacrh ü yazmak zorundayiz

def tersten_Arama(sozluk,deger):
    for key in sozluk:
        if sozluk[key] == deger:
            print("Vardir")
            return key
    else:
        #raise KeyError("Deger bulunamadi")#-->exception
        raise LookupError("Deger bulunamadi")#-->exception
sozluk={
    "a":2,
    "b":4,
    "c":14,
    "d":7
}
tersten_Arama(sozluk,4)