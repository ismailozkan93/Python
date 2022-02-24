#Kelimeleri okumak icin
#*open() fonksiyonu
    #open(file,mode)
    #burada mode:
        #*r:read(default)
        #*a:append
        #*w:write
        #*x:create

#open() fonksiyonu ile bir dosya acalim--> file nesnesi verir
file=open("metin.txt")
print(file.readline())#ilk satir
print(file.readline())#ikinci satir
#\n:yeni satir new line
#\r:enter tusu(carriage return)
file=open("metin.txt") #basa döner
print("************")
for index,line in enumerate(file):
    if index<15:
        kelime_dizisi=line.split()#split() (space,\n,\r,\t) gibi karakterleri ayirir
        print(index,kelime_dizisi)
    else:
        break