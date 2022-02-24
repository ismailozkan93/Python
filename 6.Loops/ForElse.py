##Bazen bir for döngüsünün düzgpn tanimlanip tanimlanmadigini kontrol ediniz
##Eger bir for döng¨s¨icin BREAK ifade cagrilmissa, ozaman düzgün calismamis demektir
##Bunun icin for-else yapisi kullanilir

print("-----For Döngüsünden Önce--------")
for i in range(2,10):
    print(i)
    if i%7==0:
        break
else:
    print("Döngü düzügn calisti")

print("----For Döngüsünden Sonra-------")

print("-----For Döngüsünden Önce--------")
for i in range(2,10):
    print(i)
    if i%17==0:
        break
else:
    print("Döngü düzgün calisti")

print("----For Döngüsünden Sonra-------")

##Döngü hic if in icinde grmedi,break olmadi
##Yani düzgün calisti-> else yapisina gelir

