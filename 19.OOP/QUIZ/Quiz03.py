"""
Aşağdaki şekilde iki class tanımlayın:
Sarki:
Şarkılarımızı tutmak için kullanacağız.
Her şarkının; 'adi', 'sanatci', 'album' ve 'sarki_no' diye özellikleri var.
'album' adlı özellik Album class'ı tipinde olacak.

Album:
Albümlerimizi tutacak.
Her albümün; 'adi', 'sanatci', 'yil' ve 'sarkilar' diye özellikleri var.
'sarkilar' bir liste olacak ve içinde Sarki nesnelerini tutacak.
Album'un içinde 'sarki_ekle()' adlı bir metod var ve bu metod albüme şarkı ekler.
Bunu yaparken bir şarkı numarası üretir ve öyle ekler.

Album içindeki şarkıları tek tek ekrana yazdırın.

İpuçları:
* önce albüm sonra şarkı üretin

Örnek Çağırma:
album = Album('Yesterday and Today', 'The Beatles', 1966)
album.sarki_ekle('Yesterday')
album.sarki_ekle('Act Naturally')
album.sarki_ekle('What Goes On')
Beklenen Sonuç:
Yesterday
Act Naturally
What Goes On
"""
class Sarki:
    def __init__(self,s_adi,s_sanatci,s_album,s_sarki_no):
        self.adi=s_adi
        self.sanatci=s_sanatci
        self.album=s_album
        self.sarki_no=s_sarki_no

    def __str__(self):
        return self.adi

class Album:
    def __init__(self,a_adi,a_sanatci,a_yil):
        self.adi=a_adi
        self.sanatci=a_sanatci
        self.yil=a_yil
        self.sarkilar=[]

    def sarki_ekle(self,sarki_adi):
        #toplam sarki sayisi
        sarki_no=len(self.sarkilar)

        #Sarki nesnesi olustur
        sarki=Sarki(sarki_adi,self.sanatci,self,sarki_no)

        #Simdi bu sarkiyi sarkilar listeye ekle
        self.sarkilar.append(sarki)

    def __str__(self):
        return self.adi

album=Album("Yesterday and Today","The Beatles",1966)
album.sarki_ekle("Yesterday")
album.sarki_ekle("Act Naturally")
album.sarki_ekle("What goes on")
print(album.sarkilar)

for sarki in album.sarkilar:
    print(sarki)

class Sanatci:
    def __init__(self,isim):
        self.isim=isim
        self.albumler=[]

    def album_ekle(self,album):
        if not album in self.albumler:
            self.albumler.append(album)

beatles=Sanatci("The Beatles")
album1=Album("Yesterday and Today","The Beatles",1966)
album1.sarki_ekle("Yesterday")
album1.sarki_ekle("Act Naturally")
album1.sarki_ekle("Adele")
beatles.album_ekle(album1)

album2=Album("Let it be","The Beatles",1970)
album2.sarki_ekle("Let it be")
album2.sarki_ekle("For You Blue")
album2.sarki_ekle("For You Yel")
beatles.album_ekle(album2)

print("*******Albumler********")
for album in beatles.albumler:
    print(album)

print("********Sarkilar********")
for album in beatles.albumler:
    for sarki in album.sarkilar:
        print(sarki)
"""

"""


