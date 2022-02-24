#FOnksiyon dönen fonksiyon
#Jenerik carpma fonksiyonu
#Parametreler:n (int)
#Return:lamd a: a * n seklinde bir lambda fonksiyon

def katini_al(n):
    return lambda a: a * n

ikili_katlar=katini_al(2)
print(ikili_katlar(15))
print(ikili_katlar(9))
besinci_katlar=katini_al(5)
print(besinci_katlar(12))