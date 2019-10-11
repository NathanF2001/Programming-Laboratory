def achar_caminho_largura(vertice_principal,N,caminhos):
        '''
        Aplica o Algoritmo de breadth first search.
        '''
        menor = 1000000000000000000000000000
        maior = 0
        fila = [] 
        visitados = [0 for a in range(N)]
        visitados[vertice_principal] = 1
        for a in self.grafo[vertice_principal]:
            visitados[a[0]] = 1
            fila.append(a)
        c = 1
        vertice_atual = fila.pop(0)
        while c<len(N):
            for a in self.grafo[vertice_atual[0]]:
                if visitados[a[0]] == 0:
                    visitados[a[0]] = 1
                    valor = (a[0],a[1]+vertice_atual[1])
                    if valor[1] > maior:
                        maior = valor[1]
                    if valor[1] < menor:
                        menor = valor[1]
                    fila.append(valor)
                    c+=1
            vertice_atual = fila.pop(0)

def grafo(caminhos,N,S):
        '''
        Coloca o grafo em uma Lista.
        '''
        
        grafo = [[] for a in range(N)]
        for a in caminhos:
            
            grafo[int(caminhos[0])].append((int(caminhos[1],caminhos[2])))
            grafo[int(caminhos[1])].append((caminhos[0],caminhos[2]))
        achar_caminho_largura(S,N,grafo)
        print(grafo)

N,M = input().split(' ')
N,M = int(N),int(M)
conexoes = []
for a in range(M):
    U,V,P = input().split(' ')
    conexoes.append((U,V,P))
S = int(input())

grafo(conexoes,N,S)
#O algoritmo iria funcionar com a busca em largura, o algoritmo iria percorrer por todos os caminhos possíveis e quando achasse um valor que fosse maior ou menor ele iria guardar na variável respectiva a ele. No final iria printar a diferença
#entre eles.

