entrada = input()
cadeia = []
tamanho = len(entrada)
for i in range(tamanho):
    for j in range(i,tamanho):
        if entrada[i:j+1] not in cadeia:
            cadeia.append(entrada[i:j+1])
print(cadeia)
