#Soru6
tuple_listesi = [(2,5,8), (4,3), (1,7,9,6), (5,)]
print('Fonksiyondan önce tuple_listesi:', tuple_listesi)

#tuple_sonunu_degistir(tuple_listesi)
print('Fonksiyondan sonra tuple_listesi:', tuple_listesi)

def tuple_son_degistir(liste):
    for index,tup in enumerate(liste):
        son_eleman_kadar=tup[:-1]
        son_eleman=tup[-1]**2
        tup=son_eleman_kadar+(son_eleman,)
        liste[index]=tup


print(tuple_son_degistir(tuple_listesi))

def tuple_karesi_ile_degistir(liste):
    yeni_liste=liste.copy()

    for index,tup in enumerate(yeni_liste):
        yeni_tup=tuple()

        for t in tup:
            yeni_tup +=(t**2,)

        yeni_liste[index]=yeni_tup

    print(yeni_liste)
    return yeni_liste

tuple_karesi_ile_degistir(tuple_listesi)

#Soru8

oyuncular = ['Marlon Brando', 'Heath Ledger', 'Natalie Portman', 'Emma Stone']
karakterler = ['Don Vito Corleone', 'Joker', 'The Swan Queen', 'Mia']
filmler = ['The Godfather', 'The Dark Knight', 'Black Swan', 'La La Land']
yillar = [1972, 2008, 2010, 2016]

# fonksiyonu çağıralım
def oyuncu_film_karakteri_yil(oyuncular, karakterler, filmler, yillar):
    oyuncu_karakter=zip(oyuncular,karakterler)
    filmler_yillar=zip(filmler,yillar)
    birlesik_zip=zip(oyuncu_karakter,filmler_yillar)
    dictionary=dict()
    for e1,e2 in birlesik_zip:
        dictionary[e1]=e2

    print(dictionary)
    print(len(dictionary))
    return dictionary

oyuncu_film_karakteri_yil(oyuncular,karakterler,filmler,yillar)
#oyuncu_film_sozluk















































