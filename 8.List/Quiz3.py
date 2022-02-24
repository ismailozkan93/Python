a=[12,4,2,1,6,3,45]
def sirala(liste,azalan_mi=False):
    sirala_liste=[]

    if azalan_mi:
        sirala_liste=sorted(liste,reverse=True)
    else:
        sirala_liste=sorted(liste)
    return sirala_liste
print(sirala(a,True))

aralik=range(20,300,5)

print(list(aralik))