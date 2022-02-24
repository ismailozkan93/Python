#Parametre olarak bir liste alan bir fonksiyon yazın. Adı **toplam** olsun.
def toplam(liste):
    sum=0
    for i in liste:
        sum +=i
    print(sum)

#list=[1,2,3,4,5]
#toplam(list)

#Parametre olarak, iç içe bir liste (nested list) alan bir fonksiyon yazın. İsmi **iki_seviye_toplam** olsun.
# Bu iç içe liste parametresi 2 seviyeli olsun.
#neslist=[[5,8],[1,4,7],[10],3]
def iki_Seviyeli_toplam(dizi):
    sum=0
    for i in dizi:
        #tip kontrolü
        if type(i) == list:
            for j in i:
                sum +=j
        elif type(i)==int:
            sum +=i
    return (sum)

#iki_Seviyeli_toplam(neslist)

liste = [[5, 8], [1, 4, 7, [8, 2]], [10, [-1, 2]], 3]
def her_Seviyeli_toplam(dizi):
    sum=0
    for i in dizi:
        if type(i)==int:
            sum +=i
        #tip kontrolü
        elif type(i) == list:
            sum += iki_Seviyeli_toplam(i)

    print(sum)

her_Seviyeli_toplam(liste)