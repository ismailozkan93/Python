#Bazen bir fonksiyonun icinde baska bir fonksiyon tanimlanamaiz gerekebilir
#Buna "NESTED FUNCTIONS"denir
#Ic ice fonksiyonlar kullanip bir sayinin 5 ve 8in ortak kati olup olmadigini bulalim

"""
#Verilen bir sayinin hem 5 ve hem de 8 in kati olup olmadigini kontrol eder
#Parametre:n (int)
#Return:hem 5 hem de 8 in kati ise TRUE,degilse False döner
#Ic fonksiyon 1: 5'e bölünmeyi kontrol edicek
#Ic fonksiyon 2: 8 e bölünmeyi kontrol edicek
"""
def ortak_kat_mi(n):

    #Ic fonksyion 1:5e bölünmeyi kontrol edecek
    def besin_kati_mi(n):
        if n%5==0:
            return True
        else:
            return False

    #Ic fonksiyon2:8'e bölünmeyi kontrol edecek
    def sekizin_kati_mi(n):
        if n%8==0:
            return True
        else:
            return False

    if(besin_kati_mi(n) and sekizin_kati_mi(n)):
        print(n)
        return True
    else:
        return False


ortak_kat_mi(40)