#Bircok zaman bir döngü icinde gezerken,döngünün o andaki elemani(iteration) icin baska bir döngü calistirmamiz gerekir
#ekrana yildizlardan kare cizelim

#satir döngüsü
i=0
while i<3:
    yildizlar=""

#sütun döngüsü
    j=0
    while j<3:
        yildizlar +="* "
        j +=1
    print(yildizlar)

    i +=1

print("********************")

#satir döngüsü
for i in range(4):
    yildizlar= ""

    #sütun döngüsü
    for j in range(6):
        yildizlar=yildizlar+"* "
    print(yildizlar)