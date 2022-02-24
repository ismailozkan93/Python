#Esitler mi
#Hangisi büyük

meyve="Armut"

if meyve=="Armut":
    print("Evet Armut")
else:
    print("Degil Armut")

armut="armut"
elma="elma"

if armut<elma:
    print("{0},{1}'dan kücüktür".format(armut,elma))
else:
    print("{0} {1}'den büyüktür".format(armut,elma))

###armut elmadan kücüktür cünkü "a" harfi "e" harfinden önce gelir
###ASCII karakteri daha kücüktür
###ASCII karakterleri icin -->ord() fonksiyonu kullanilir

print("a:",ord("a"))
print("A:",ord("A"))
print("z:",ord("z"))
print("Z:",ord("Z"))
print("c:",ord("c"))
print("C:",ord("C"))

##ascii 'YE göre bütün büyük harfler,kücük harflerden önce gelir
