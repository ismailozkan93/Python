#string.punctuation---> noktalama isaretlerini cikaralim
#string.whitespace -->bosluk karakterini cikaralim
#kitaplarin baslangic ve sonunu bulalim
#her islemi kendi fonksiyonunda yapalim
#string modulünü kullanalim

#Genelde import islemleri
import string
from collections import Counter

noktalama_isaretleri=string.punctuation#global degisken
print(noktalama_isaretleri)
bosluk=string.whitespace#global degisken
print(bosluk)
kitap_adi="Alice"
def dosyadan_oku(kitap_adi):
    kitap_yolu=(kitap_adi+".txt")
    return open(kitap_yolu,encoding="utf-8")
#Kitap Okuma Fonksiyonu
def kitap_oku(kitap_adi):
    kelimeler=list()
    #önce file olarak kaydedelim
    file=dosyadan_oku(kitap_adi)

    #Verilen satiri atlar
    baslangic_atla(file)

    #Simdi kelimeleri dolduralim
    kelimeleri_doldur(file,kelimeler)
    return kelimeler

##baslangc bölümünü atlar
def baslangic_atla(file):
    atlama_metni="When the papers were exhausted, the conversation of the Palmers became more steady and personal."#Line41
    for line in file:
        if line.startswith("When the papers were exhausted, the conversation of the Palmers became more steady and personal."):
            break

def sona_gelindi_mi(line):
    bitirme_metni="“Are you kiddin’ me?” demanded his father."
    return line.startswith(bitirme_metni)

def satirdaki_kelimeler(satir):#Satirdaki kelimeleri getiren fonksiyon
    satir_kelimeleri=[]
    kelime_dizisi=satir.split()
    for kelime in kelime_dizisi:
        kelime=kelime.strip(noktalama_isaretleri)#Eger kelimede noktalama isareti varsa
        kelime=kelime.lower()#kücük harf yap
        if kelime.isalpha() and len(kelime)>0:  #alfanumerik mi
            satir_kelimeleri.append(kelime)
    return satir_kelimeleri

def kelimeleri_doldur(file,kelimeler):
    for line in file:
        if not sona_gelindi_mi(line):
            #satir icindeki kelimeleri al
            satir_kelimeleri=satirdaki_kelimeler(line)
            kelimeler.extend(satir_kelimeleri)

Alice_kelimeleri=kitap_oku(kitap_adi)

def liste_sirala(liste,azalan_mi):
    #Uzunluk ile siralayacaksak -->key parametresi vermemiz lazim-->lambda
    return sorted(liste,reverse=azalan_mi,key=lambda x: len(x))

print(liste_sirala(Alice_kelimeleri,True))

def tekrarlari_sil(liste):
    kume=set(liste)#set tekrarli cikarir

    #sonra tekrar list
    tekrarsiz_liste=list(kume)
    return tekrarsiz_liste

def kelime_sayisi(liste):
    return len(liste)

print(kelime_sayisi(Alice_kelimeleri))
print(kelime_sayisi(tekrarlari_sil(Alice_kelimeleri)))

#En yüksek adetli n kelimeyi veren fonksyion
def en_yuksek_adetli(liste, n=20):
    #Sözlük olarak dönecek
    kelime_adetleri={
        kelime:liste.count(kelime)
        for kelime in liste
    }
    sirali_liste=sozluk_sirala(kelime_adetleri)

    sirali_liste_top_n=sirali_liste[:n]

    return dict(sirali_liste_top_n)

def sozluk_sirala(sozluk):
    #sorted(--> geriye liste döner

    sirali_liste=sorted(sozluk.items(),key=lambda x:x[1], reverse=True)

    return sirali_liste

alice_kelime_Adet=en_yuksek_adetli(Alice_kelimeleri)
print(alice_kelime_Adet)



