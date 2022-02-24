#Bir fonksiyonu baska fonksiyonlari cagirdigi gibi,kendisini de cagirabilir
#Buna **RECURSION** adi verilir
#Verilen bir sayidan geriye dogru, 0'a kadar sayan bir fonksiyon

#Önemli Not::Recursionlarda **durma kosulu** cok önemlidir,aksi takdirde SONSUZ DÖNGÜYE  girer

def geri_say(n):
    #ilk önce durma kosulunu yazmamiz lazim
    if n<=0:
        print("----THE END------")
    else:
        print(n)
        geri_say(n-1)

geri_say(4)

#Kendisine verilen metni geriye dogru sayarak yazan bir fonksiyon tanimlayalim
def metin_geriye(metin,n):
    #önce durma kosulu
    if n<=0:
        print("---THE END----")
        return      #DURMA KOSULU islevi görür
    else:
        print("{0}:{1}".format(n,metin))
        metin_geriye(metin,n-1)

metin_geriye("Machine Laerning",5)