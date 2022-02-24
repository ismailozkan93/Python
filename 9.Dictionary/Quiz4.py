"""
Parametre olarak iki liste alan bir fonksiyon yazın. Fonksiyonunuzun adı **listeleri_sozluk_yap** olsun.
Fonksiyon ilk listedeki elemanları key, ikinci listedeki elemanları value yaparak ikisinden bir dictionary üretsin.
Parametreler:
l_1 = ['ad', 'soyad', 'yas', 'cinsiyet']
l_2 = ['John', 'Doe', 100, 'Erkek']
Sonuc:
{'ad': 'John', 'soyad': 'Doe', 'yas': 100, 'cinsiyet': 'Erkek'}
"""
l_1 = ['ad', 'soyad', 'yas', 'cinsiyet']
l_2 = ['John', 'Doe', 100, 'Erkek']
def listeleri_sozluk_yap(list1,list2):
    sozluk=dict()
    for index,e in enumerate(list1):
        sozluk[e]=list2[index]
    return sozluk

print(listeleri_sozluk_yap(l_1,l_2))

#Soru10
sozluk={'a': 'A', 'b': 'B', 2: 200, 'd': 'D', 5: 300, 'f': 'F', 1: 50}
def alfanumeric(dict):
    deleted_dict=[]
    for key in dict.keys():
        if not str(key).isalpha():
            deleted_dict.append(key)
    for key in deleted_dict:
        if key in dict.keys():
            dict.pop(key)

    return dict

print(alfanumeric(sozluk))