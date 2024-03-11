n = int(input())
trg = []
for i in range(n+1):
    trg.append([1]+[0]*n)
for i in range(1,i+1): # i +1 чтобы доходить до главной диаганали и не проходить по нулям
    for j in range(1,n+1):
        trg[i][j] = trg[i-1][j]+trg[i-1][j-1]
        print(trg[i][j], end=' ')
    print()
