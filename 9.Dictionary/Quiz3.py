"""
**Soru 6:**
Verilen iki sözlüğü içinde key'leri aynı olan elemanların değerlerini toplayan bir fonksiyon yazın.
Eğer key ikisinde ortak değilse almasın, sadece ortak key'leri alsın.
Fonksiyonun adı **** olsun.

**İpuçları**
* Parametrelerin ikisinin de sözlük olmasını kontrol edin
    * değilse hata fırlatın -> 'Parametrelerin ikisi de sözlük olmalı'
    * kontrol için -> 'type' yerine bu sefer 'isinstance' kullanın
    * isinstance(<değişken>, <tip>)
* Sözlüklerin uzunluklarının aynı olmasını kontrol edin
    * değilse hata fırlatın -> 'Sözlüklerin uzunluğu aynı olmalı'
Sonuç:
 #raise KeyError("Deger bulunamadi")#-->exception
        raise LookupError("Deger bulunamadi")#-->exception
{'a': 50, 'b': 90}
"""
d1 = {'a': 10, 'b': 30, 'c':50}
d2 = {'a': 40, 'b': 60, 'd':90}

def ayni_key_toplamlari(d1,d2):
    yeni_sozluk={}
    if not (isinstance(d1,dict) or isinstance(d2,dict)):
        raise LookupError("d1 ve ve d2 sözlük olmalidir")

    if not (len(d1)==len(d2)):
        raise Exception("Parametrelerin ikisi de sözlük olmali")

    for key in d1:
        if key in d2:
            yeni_sozluk[key]=d1[key]+d2[key]

    return yeni_sozluk

print(ayni_key_toplamlari(d1,d2))

def ayni_key_toplamlari_farkli_key_kendileri(d1, d2):
    yeni_sozluk={}
    if not (isinstance(d1,dict) or isinstance(d2,dict)):
        raise LookupError("d1 ve ve d2 sözlük olmalidir")

    if not (len(d1)==len(d2)):
        raise Exception("Parametrelerin ikisi de sözlük olmali")

    for key in d1:
        if key in d2:
            yeni_sozluk[key]=d1[key]+d2[key]
        else:
            if key in d1:
                yeni_sozluk[key]=d1[key]

            for key in d2:
                if not key in d1:
                    yeni_sozluk[key]=d2[key]
    return yeni_sozluk
print(ayni_key_toplamlari_farkli_key_kendileri(d1, d2))

"""
Verilen bir dictionary içindeki tek index'li elemanları silip geriye sadece çift index'li elemanların olduğu yeni bir dictionary dönen bir fonksiyon yazın.
Fonksiyonun adı **tekleri_sil** olsun.
**İpuçları:**
* Parametre olarak gelen orijinal dictionary'ye dokunmayın.
* döngü için `items()`
* index için `enumerate()`
sozluk = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F'}
Sonuç:
 {'a': 'A', 'c': 'C', 'e': 'E'}
"""
sozluk = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F'}
def tekleri_sil(sozluk):
    sozluk_yeni={}
    for index,item in enumerate(sozluk.items()):
        key=item[0]
        value=item[1]
        if(index%2==0):
           sozluk_yeni[key]=value
    return sozluk_yeni
tekleri_sil(sozluk)

print(tekleri_sil(sozluk))

##2nci yol
def tekleri_sil2(sozluk):
    sozluk_yeni={}
    for index,item in enumerate(sozluk.items()):
        if(index%2==0):
            sozluk_yeni.update({item})

    return sozluk_yeni

print(tekleri_sil2(sozluk))