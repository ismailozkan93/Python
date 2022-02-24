#satir döngüsü
n=int(input("Sayi giriniz"))
def kare(n):
    i=0
    while i<n:
        yildizlar=""

#sütun döngüsü
        j=0
        while j<n:
            yildizlar +="* "
            j +=1
        print(yildizlar)
        i +=1


#kare(n)

#Soru2
def kare1(n):
    for i in range(n):
        yildizlar = ""

        # sütun döngüsü
        for j in range(n):
            yildizlar = yildizlar + "* "
        print(yildizlar)

#kare1(n)

#Soru3
#satir döngüsü
n=int(input("Sayi giriniz"))
def ücgen(n):
    i=0
    while i<n:
        yildizlar=""

#sütun döngüsü
        j=0
        while j<=i:
            yildizlar +="* "
            j =j+1
        print(yildizlar)

        i +=1

#ücgen(n)

#Soru 4
def ucgen1(n):
    for i in range(n):
        yildizlar = ""

        # sütun döngüsü
        for j in range(i+1):
            yildizlar = yildizlar + "* "
        print(yildizlar)


#ucgen1(6)
def ücgen2(n):
    for i in range(n,0,-1):
            yildizlar=""
            for j in range(i):
                yildizlar +="* "
            print(yildizlar)

def ikizkenar(n):
    ucgen1(n-1)
    ücgen2(n)


ikizkenar(n)
