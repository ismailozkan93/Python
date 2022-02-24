#Matematiksel islemler icin Math modulu kullanilir
#Modül:birbirleriyle ilgili fonksiyon ve dosyalari bir arada tutan dosya kümeleridir
#math modulü iceri alinir
import math
#math modülünü görelim
print(math);
#help(math);

#bir modül icindeki bir fonksiyonu --> .ile cagrilir
print(math.pi);
#Ornk:yaricapi 10 olan bir cemberin cevresini hesaplayiniz
r=10
Cevre=(2*(math.pi)*r)
print(Cevre)

#3O derecenin Sinüsünü hesaplayalim
derece=30
#radyan hesapla
radyan=math.radians(derece)
print(radyan)

sinus=math.sin(derece)
print(sinus)#cevap dogru degildir sinus fonksiyonu radyan ile calisir

sinus1=math.sin(radyan)
print(sinus1)
#FOnksiyonlarin birlesimi
derece=30
sinus2=math.sin(math.radians(derece))#Chain :Fonksiyonu zincirlemek
print(sinus2)