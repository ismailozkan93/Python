class Nokta:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

#Iki noktasi nesnesi olustur
n1=Nokta(2,5)
n2=Nokta(-1,4)

#Python'da print()-->__str__()methodu getirir
#default olarak object ten gelir
print("----Overload Öncesi-----")
print(n1.__str__())
class Nokta(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    #___str__() methodunu ezdik yani overloading ettik
    def __str__(self):
        return "Bu bir noktadir,koordinatlari: {0}x{1}".format(self.x,self.y)

print("-----------Overloading Sonrasi----------")
n1=Nokta(2,5)
print(n1)

print(Nokta.__name__)

