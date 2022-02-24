"""
n=input("Lütfen sayi giriniz")
def asal_mi(n):
    asal=True
    for i in range(2,n):
        if (n%i==0):
            print("Asaldir")
            asal=False

        else:
            print("Asal degildir")
            asal=True

    return asal

asal_mi(n)
"""

def asal_carpanlar(n):
    for i in range(2,n):
        if n%i == 0:
            print(i)
