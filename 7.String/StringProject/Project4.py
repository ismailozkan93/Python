##Eger bir kelimenin harfleri alfabetik sirada ise, bu kelimeye **düzgün kelime ** diyelim
##düzgün true degilse false döndürelim

def duzgun_kelime_mi(kelime):
    önceki=kelime[0]

    for harf in kelime:
        if harf <önceki:
            return False
        önceki=harf

     #print("Düzgün bir kelimedir")
    return True

def lorem_düzgün_mü():
    file=open("metin.txt")

    for index,line in enumerate (file):
        if duzgun_kelime_mi(line)==True:
            print(index,line,"düzgün kelimedir")

lorem_düzgün_mü()