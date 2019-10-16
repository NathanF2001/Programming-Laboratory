def achar_maior_e_menor_caminho(vertice_principal,N,caminhos):
    '''
        Algoritmo de achar o menor e maior caminho ( Baseado na busca em largura/ Algoritmo de Dijskara.
    '''
    fila = [] # A fila da busca
    inicio = vertice_principal # Começa com o servidor
    visitados = [None for a in range(N)] # Arranjo de vertices visitados
    visitados[vertice_principal] = -1 # Parâmetro para que dizer que o vertice foi visitado
    for a in caminhos[vertice_principal]: # Calcular a distância até os vizinhos do servidor
        visitados[a[0]] = a[1] #Visitados vai guardar a distância para que fique mais fácil de comparar.
        fila.append(a)#Adicionar a fila de prioridade
    vertice_atual = min(fila,key = lambda x: x[1]) #Achar o caminho mais curto( Baseado Dijskara)
    fila.remove(vertice_atual)#Retira da lista da fila

    while True:
        if fila == []: # Enquanto todos os caminhos não forem pecorridos
            if None in visitados: # Caso todos caminhos possíveis foram feito e sobrou um vertice ( nesse caso ele ta isolado)
                for p,a in enumerate(visitados):
                    if a == 0:
                        vertice_atual[p] = -1 #Coloca como visitado
                        break
            else:
                break

        for a in caminhos[vertice_atual[0]]: # Percorre os vertices vizinhos ao vertice que está no momento
            if visitados[a[0]] == None:# Caso não foi visitado nenhuma vez
                visitados[a[0]] = a[1]+vertice_atual[1] # Adiciona o caminhos até o vertice mais a distancia até o vizinho
                valor = (a[0],a[1]+vertice_atual[1]) # Valor para adicionar a lista de busca
                fila.append(valor)
            else:   #Caso ja tenha sido visitado
                if a[0]!=inicio and a[1] + vertice_atual[1] < visitados[a[0]]:# Se o caminho for menor ao caminho ja percorrido
                    posição = find_way(fila,(a[0],visitados[a[0]]))
                    #fila.remove((a[0],visitados[a[0]]))# Retiro o item na lista de Busca
                    #fila.append((a[0],a[1] + vertice_atual[1]))# Adiciono o novo caminho
                    fila[posição] = (a[0],a[1] + vertice_atual[1])
                    visitados[a[0]] = a[1] + vertice_atual[1]
        vertice_atual = min(fila,key =lambda x: x[1])
        fila.remove(vertice_atual)


    return visitados # Retorna todos os menores caminhos para cada vertice em relaçao ao servidor

def find_way(array,value):
    for p,a in enumerate(array):
        if a == value:
            return p

def grafo():
        '''
        Coloca o grafo em uma Lista.
        '''
        N,M = map(lambda i: int(i),input().split(' '))
        grafo = [[] for a in range(N)]
        for a in range(M):
            U,V,P = map(lambda i: int(i),input().split())
            grafo[U-1].append((V-1,P))
            grafo[V-1].append((U-1,P))
        S = int(input())

        return achar_maior_e_menor_caminho(S-1,N,grafo)

a = grafo()
maior = None
menor = None
for k in a:
    if k != -1:
        if maior is None:
            maior = k
        if menor is None:
            menor = k
        if k > maior:
            maior = k
        if k < menor:
            menor = k

print(maior-menor)

