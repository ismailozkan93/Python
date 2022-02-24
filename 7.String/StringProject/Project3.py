def hepsini_kullanir(metin,harfler):
    tumunu_kullanir=True
    for harf in harfler:
        if not harf in metin:
            print("Hepsi kullanilmamistir")
            tumunu_kullanir=False

    return tumunu_kullanir

#print(hepsini_kullanir("Araba demir yolundan gecti","aezbd"))
def lorem_hepsi_kullanilmis_mi():
    file = open("metin.txt")
    for index,line in enumerate(file):
        if hepsini_kullanir(line,"rem"):
            #print(index,line)
            print("Txt 'de ",index ," de bu verilen harfleri hepsi kullanilmamistir")


lorem_hepsi_kullanilmis_mi()