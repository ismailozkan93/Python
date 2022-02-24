#Sartli Ifadeler
#Bu böülümde if-else yapisini görecegiz
#Sartli ifadeler mantiksal operatörler ile kontrol edilir

#Tek esit ->= atama demektir
a=6

#esitlik kontrolü
a==6 #True
a==8 #False

type(True) #bool
type(False) #bool

#SART OPERATÖRLERI
"""
x==y:x,y'ye esit midir?
x!=y:x,y'ye esit degil midir?
x<y:x,y'den kücük müdür?
x>y:x,y'den büyük müdür?
x<=y:x,y'den kücük esit midir?
x>=y:x,y'den büyük esit midir?
"""
x=12
y=8

print("x==y:",x==y)
print("x!=y:",x!=y)
print("x<y:",x<y)
print("x>y",x>y)
print("x<=y",x<=y)
print("x>=y",x>=y)
#And--OR
a=False
b=True
print("-----and-----")
print("{0} and {1}: {2}".format(a, b, a and b))
print("{0} or {1}: {2}".format(a,b,a or b))


