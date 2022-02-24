##Iki elemanin ortak elemanlarin bulmak icin --<Kesisim Kümesi-->intersection
notlar=["A","B","C","D","E"]
notlar_seti=set(notlar)
dereceler=set({"A","B","K","T","E"})

ortaklar=notlar_seti.intersection(dereceler)
print(ortaklar)

#Birlesim UNION
birlesim=notlar_seti.union(dereceler)
print(birlesim)

#Fark-->difference
A_fark_B=notlar_seti.difference(dereceler)
print(A_fark_B)

B_fark_A=dereceler.difference(notlar_seti)
print(B_fark_A)

#issubset()-->alt küme mi
print(notlar_seti.issubset(dereceler))
a=set({"a","b",2})
b=set({"b","a"})
print(b.issubset(a))

#issuperset() üst kümesi mi
print(a.issuperset(b))

##Symmetric_difference():
#Iki kümenin karsi ayrik kümeleri
print(notlar_seti.symmetric_difference(dereceler))
















