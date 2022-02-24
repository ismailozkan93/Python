def tamamen_farkli_mi(set1,set2):
    if not isinstance(set1,set) or not isinstance(set2,set):
        raise Exception("Parametreler Set tipinde degil")
    else:
        if set1.isdisjoint(set2):
            return "Bu iki küme tamamen farkli"
        else:
            return "Tamamen farkli degil,ortak elemanlar var"+set1.intersection(set2)



"""
arametre olarak bir küme alan bir fonksiyon yazın. Adı **kopyala_ve_temizle** olsun.

Fonksiyon parametre olarak gelen kümeyi boşaltsın ama değerlerini yeni bir küme olarak geri dönsün.

Yani parametre yerinde değişip boş küme olacak ama değerleri ise başka bir küme olarak geri dönecek.

**İpuçları:**
* döngü kullanmayın
* copy()
* clear()

<pre style="background: gold">
Parametre:
set1 = {'A', 'B', 'C', 'D', 'E'}

Sonuç:
fonksiyon çağırmadan önce set1: {'E', 'C', 'D', 'B', 'A'}
fonksiyon çağırdıktan sonra set1: set()
"""
set1={'E', 'C', 'D', 'B', 'A'}
def kopyala_ve_temizle(kume):
    yenikume=kume.copy()
    kume.clear()
    print(yenikume)
    return yenikume

kopyala_ve_temizle(set1)

kume1 = {'a', 'b', 'c', 'd', 'e', 'f'}
kume2 = {'d', 'b', 'e', 'f', 'h', 'g'}

def ayni_olanlari_sil(kume1,kume2):
    kume1.difference_update(kume2)
    print(kume1)
ayni_olanlari_sil(kume1,kume2)


#Soru10
#def hangi_üst_küme(kum1,kum2):




















