tekler=[]

for i in range(1,11):
    if(i%2)==1:
        tekler.append(i)

print(tekler)

tekler_comp=[i
             for i in range(1, 11)
             if (i % 2) == 1
    ]
print(tekler_comp)

carpanlar={}

for i in range(2,21):
    for j in range(2,i+1):
        if i%j==0:
            if not i in carpanlar:
                carpanlar[i]=[j]
            else:
                carpanlar[i].append(j)
print(carpanlar)

carpanlar_compf={
    i:[j for j in range(2,i+1) if i%j==0]
    for i in range(2,21)
}
print(carpanlar_compf)

carpanlar_cift={}
for i in range(2,21):
    if i%2==0:
        for j in range(2,i+1):
            if i%j==0:
                if not i in carpanlar:
                    carpanlar[i]=[j]
                else:
                    carpanlar[i].append(j)

print(carpanlar_cift)

carpanlar_cift_compf={
            i:[j for j in range(2,i+1) if i%j==0]
            for i in range(2,21)
            if i%2==0
}

