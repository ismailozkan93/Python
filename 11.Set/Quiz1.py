eklenecek_meyve=['Vişne', 'Kiraz', 'Kayısı', 'Karadut']
def kume_create(liste):
    meyve=set({"Elma", "Armut", "Karpuz", "Çilek"})

    for e in liste:
        meyve.add(e)

    print(meyve)
    return meyve

kume_create(eklenecek_meyve)

#Soru2
def kume_create_tek_sefer(liste):
    meyve = set({"Elma", "Armut", "Karpuz", "Çilek"})
    meyve.update(liste)
    print(meyve)
    return meyve

kume_create_tek_sefer(eklenecek_meyve)

#Soru3
set1 = {10, 20, 30, 40, 50, 60}
set2 = {20, 40, 60, 80, 90, 100}
def ayni_elemanlar(set1,set2):
    ortak_eleman=set1.intersection(set2)
    ortak_eleman =sorted(ortak_eleman)
    print(ortak_eleman)
    return ortak_eleman

ayni_elemanlar(set1,set2)

#Soru4
set1 = {10, 20, 30, 40, 50, 60}
set2 = {20, 40, 60, 80, 90, 100}
def tum_elemanlar(kume1,kume2):
    toplam_eleman=kume1.union(kume2)
    toplam_eleman=sorted(toplam_eleman, reverse=True)
    print(toplam_eleman)

tum_elemanlar(set1,set2)

#Soru5
l_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l_2 = [2, 4, 6, 8]
def farki_ver(liste1,liste2):
    #listleri set'e cevir
    set_1=set(liste1)##listi sete cevirir
    set_2=set(liste2)
    differ=set_1.difference(set_2)
    print(differ)

farki_ver(l_1,l_2)

set_1 = {20, 10, 40, 30, 50}
set_2 = {60, 80, 70, 100, 90}
def tamamen_farkli_mi(set1, set2):
    if not (set1 is set2):
        return "FARKLIDIR"

print(tamamen_farkli_mi(set_1,set_2))
##isdisjoint()--->TAMAMEN FARKLIDIR












































































