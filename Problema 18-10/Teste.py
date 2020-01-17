N,M = map(lambda i: int(i),input().split(' '))
infinity = 99999999999999999999999
grafo = [[infinity for b in range(N)] for a in range(N)]
for a in range(N):
    grafo[a][a] = 0
for a in range(M):
    U,V,W = map(lambda i: int(i),input().split(' '))
    grafo[U][V] = grafo[V][U] = W

for k in range(N):
    for i in range(N):
        for j in range(N):
            if grafo[i][j] > grafo[i][k] + grafo[k][j]:
                grafo[i][j] = grafo[i][k] + grafo[k][j]

maior = infinity
for a in grafo:
    maior_subgrafo = 0
    for b in a:
        if b>maior_subgrafo:
            maior_subgrafo = b
    if maior_subgrafo < maior:
        maior = maior_subgrafo

print(maior)
