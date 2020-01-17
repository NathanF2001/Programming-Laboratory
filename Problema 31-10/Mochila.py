itens,capacidade = map(lambda i: int(i),input().split(' '))
Peso = [0]*(itens+1)
Valor = [0]*(itens+1)
matriz = [[0 for j in range(capacidade+1)] for i in range(itens+1)]
for a in range(1,itens+1):
    peso,valor = map(lambda i: int(i),input().split(' '))
    Peso[a] = peso
    Valor[a] = valor

for peso in range(1,capacidade+1):
    for item in range(1,itens+1):
        possivel_valor_a_carregar = matriz[item-1][peso]
        if Peso[item]>peso:#Caso o peso do item seja superior a capacidade da mochila no momento
            matriz[item][peso] = possivel_valor_a_carregar#O valor a pegar será igual ao acima dele na matriz
        else:
            maximo_possivel = matriz[item-1][peso-Peso[item]]+Valor[item]#Calcula o valor do item mais o valor maximo da capacidade restante
            if possivel_valor_a_carregar > maximo_possivel:#Essa condição funciona como max
                matriz[item][peso] = possivel_valor_a_carregar
            else:
                matriz[item][peso] = maximo_possivel
        #print(peso,item,matriz[item][peso],possivel_valor_a_carregar,maximo_possivel,matriz[item-1][peso-Peso[item]],Valor[item])

print(matriz[itens][capacidade])
