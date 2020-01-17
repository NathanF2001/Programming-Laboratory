Palavras_dicionario,Palavras_analisadas = map(lambda i: int(i), input().split())
dicionario = [None]*Palavras_dicionario
maior_palavra_dicionario = 0
for a in range(Palavras_dicionario):
    dicionario[a] = input()
    if len(dicionario[a]) > maior_palavra_dicionario:
        maior_palavra_dicionario = len(dicionario[a])

maior_palavra_digitada = 0        
words = [None]*Palavras_analisadas
for a in range(Palavras_analisadas):
    words[a] = input().strip()
    if len(words[a]) > maior_palavra_digitada:
        maior_palavra_digitada = len(words[a])

        

matriz = [[0 for j in range(maior_palavra_dicionario+1)]for i in range(maior_palavra_digitada+1)]
for i in range(1,maior_palavra_dicionario+1):
    matriz[0][i] = i
for j in range(1,maior_palavra_digitada+1):
    matriz[j][0] = j


for palavra in words:
    for dic_palavra in dicionario:
        tamanho_palavra_digitada = len(palavra)
        tamanho_palavra_dicionario = len(dic_palavra)
        for i in range(1,tamanho_palavra_digitada+1):
            for j in range(1,tamanho_palavra_dicionario+1):
                if dic_palavra[j-1] == palavra[i-1]:
                    matriz[i][j] = matriz[i-1][j-1]
                else:
                    if matriz[i-1][j] > matriz[i][j-1]:
                        menor = matriz[i][j-1]
                    else:
                        menor = matriz[i-1][j]
                    if matriz[i-1][j-1] < menor:
                        menor = matriz[i-1][j-1]
                    matriz[i][j] = menor+1
                        
        if matriz[tamanho_palavra_digitada][tamanho_palavra_dicionario]<= 2:
            print(dic_palavra,end = ' ')
    print()
