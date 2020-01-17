Linhas,Colunas,Linha_desejada,Coluna_desejada = map(lambda i: int(i), input().split(' '))
matriz = [[0 for a in range(Colunas+1)] for b in range(Linhas+1)]

for a in range(1,Linhas+1):
    submatriz = input().split()
    for b in range(1,Colunas+1):
        Cajus = int(submatriz[b-1])  #Quantidade de caju na posição matriz[a][b-1]
        Cajus_acima = matriz[a-1][b]  #quantidade de cajus no retangulo de dimensão (a-1xb)
        Cajus_esquerdo = matriz[a][b-1]   #quantidade de cajus no retangulo de dimensão (a,b-1)
        Excesso = matriz[a-1][b-1]    #Existe uma região que e contada duas vezes pela interseção do dois retangulo,então pegar esse valor para retirar uma vez
        matriz[a][b] = Cajus + Cajus_acima + Cajus_esquerdo - Excesso

area_maxima = 0

for i in range(Linha_desejada,Linhas+1):
    for j in range(Coluna_desejada,Colunas+1):
        Extremidade_esquerda_baixo = matriz[i][j]   #Pega a coordenada mais extrema na região que queira pegar
        Cajus_acima = matriz[i-Linha_desejada][j]   #Demarca a região acima da Linha_desejada para que seja desconsiderada
        Cajus_esquerdo = matriz[i][j-Coluna_desejada]   #Demarca a região a esquerda da Coluna desejada para que seja desconsiderada
        Excesso = matriz[i-Linha_desejada][j-Coluna_desejada]   #A interseção dos dois quadrado vai retirar um valor duas vezes,portanto pega esse valor para adicionar
        area = Extremidade_esquerda_baixo - Cajus_acima - Cajus_esquerdo + Excesso
        if area > area_maxima:
            area_maxima = area

print(area_maxima)

