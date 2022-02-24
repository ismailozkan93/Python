liste=["a","b","c","d","e","f"]
print(liste[2:5])
print(liste[:])

#Liste Kopyalama
#->Kopyalamak->yeni bir liste almak demektir
yeni_liste=liste[:]
print(yeni_liste)
baska_liste=liste[:]
print(baska_liste)
#liste -yeni_liste-baska_liste farkli 3 elamandir
#listenin index 1,2 degistir
liste[1:3]=[10,20]
yeni_liste[0]="AA"
print(liste)
print(yeni_liste)
print(baska_liste)

#ID YÖNTEMI
#Python da tüm nesneler id ile tutulur
#Nesnenin bellekteki adrei
#id degeri->id()fonksyionu ile bulunur
print(id(liste))
print(id(yeni_liste))
print(id(baska_liste))
