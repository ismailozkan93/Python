list=[1,3,5,7,9]

def kare(liste):
    list_yeni=[0,0,0,0,0]
    for index,e in enumerate(liste):
        list_yeni[index]=e**2

    print(list_yeni)
    return list_yeni

kare(list)

#Tek indeksler 1,3,5 toplami cift indexler 0,2,4
list1 = [1, 2, 3, 4, 5, 6]
def tek_cift_index_farki(liste):
    sum_cift=0
    sum_tek=0
    fark=0
    for index,eleman in enumerate (liste):
       if index%2==0:
           sum_cift +=eleman
       else:
           sum_tek +=eleman
    fark=sum_cift-sum_tek
    print(fark)
tek_cift_index_farki(list1)
list2 = [1,"A", 2,True,"t" ,3, 4,"zE", 5, 6]
def kirpan(dizi):
    dizi.pop(0)
    dizi.pop(len(list2)-1)
    print(dizi)
kirpan(list2)