##Alising(Yeni Bir Ad Verme)
##Python'da Tip Türleri

#Primitive Tipler:int,float,string,boolean
#Non-Primitive Tipler:list,dict,tupe
#Primitive Tipler
x=24
y=x
print(x is y)
y=40
print(x is y)

#Non-Primitive Tipler
a=[1,2,3,4,5,6]
b=a
print(a)
print(b)
print(a is b) #normalde ayni olmuyordu b yi a ya atayinca ayni id oldu
                    ##***Atama yapinca degerler ayriliyor,esitlik bozuluyor
b=[10,20,30,40]
print(a,b)
print(a==b)
print(a is b)

##EGER NON-Primitive MUTATE etseydik
c=[1,2,3,4,5,6]
d=c
print(c,d)
d[0]="A"
d[1]="B"
print(c,d)      #Non-Priitiveleri Mutate ettigimizde degerler esit olur
print(c is d)

#NON PRIMITIVE tiplerde atama islemi normal degil
#BIR "YENIDEN ADLANDIRMA ISLEMI"(ALISING)
