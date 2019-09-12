class Menor_Caminho:

    def __init__(self):
        self.__grafo()
        
    def __grafo(self):
        '''
        Coloca o grafo em uma Lista.
        '''
        self.tamanho,inicio,fim = map(lambda i: int(i), input().split(' '))
        self.grafo = [[] for a in range(self.tamanho)]
        for a in range(self.tamanho-1):
            cidade_1,cidade_2,distancia = map(lambda i: int(i), input().split(' '))
            self.grafo[cidade_1-1].append((cidade_2-1,distancia))
            self.grafo[cidade_2-1].append((cidade_1-1,distancia))
            
        self.__achar_caminho_largura(inicio-1,fim-1)

    def __achar_caminho_largura(self,vertice_principal,fim):#função para analisar as cidades vizinhas
        '''
        Aplica o Algoritmo de breadth first search.
        '''
        fila = [] # Fila de prioridade das cidades que irão ser analisada
        visitados = [0 for a in range(self.tamanho)]# Lista que representa se a província foi visitada
        visitados[vertice_principal] = 1
        for a in self.grafo[vertice_principal]:#Pega todos vizinhos da primeira cidade
            visitados[a[0]] = 1
            fila.append(a)
        vertice_atual = fila.pop(0)
        while vertice_atual[0] != fim:# Enquanto não encontra o destino
            for a in self.grafo[vertice_atual[0]]:
                if visitados[a[0]] == 0:
                    visitados[a[0]] = 1
                    valor = (a[0],a[1]+vertice_atual[1])
                    fila.append(valor)
            vertice_atual = fila.pop(0)

        return print(vertice_atual[1])
                  

Menor_Caminho()



