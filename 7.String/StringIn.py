#IN Operatorü
#Bir karakter ya da metnin baska bir metin icinde olup olmadigini kontrol etmek icin kullanilir
#Varsa True döner

agac="ahlat agaci"
at="at"
print(at in agac)
print("a" in agac)
print("b" in agac)

if at in agac:
    print(agac+" icinde "+ at +" vardir" )
else:
    print(agac + " icinde " + at + " yoktur")

def a_var_mi():
    str=input("Lütfen bir cümle yaziniz")
    if("a" in str):
        print("cümlede a vardir")
    else:
        print("cümlede a yoktur")

a_var_mi()

def b_var_mi():
    str = input("Lütfen bir cümle yaziniz")
    for harf in str:
        if(harf=="b"):
            print("Cümlede b harfi vardir")
            return True

    return False

b_var_mi()


