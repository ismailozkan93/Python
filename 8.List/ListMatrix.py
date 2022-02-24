#Matrix ic ice listelerden olusur
A=[["A","B","C"],["D","E","F"],["G","H","I"]]
print(A)
B=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
   ]
print(B)

C=[
    [20,10,30],
    [60,30,70],
    [80,50,90]
   ]
print(C)
#mATRISLERDE toplama eleman bazli olmali
D=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(len(B)):
    for j in range(len(C)):
        D[i][j]=B[i][j]+C[i][j]
print(D)