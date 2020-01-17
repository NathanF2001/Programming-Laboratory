class Nodulo:

    def __init__(self,value=None,proximo = None):
        self.value = value
        self.proximo = proximo

    def get_value(self):
        return self.value

    def set_value(self,i):
        self.value = i
        
    def get_proximo(self):
        return self.proximo

    def set_proximo(self,i):
        self.proximo = i


class L:

    def __init__(self):
        self.vazio = Nodulo()
        self.vazio.set_proximo(self.vazio)
        self.primeiro = self.vazio

    def __str__(self):
        if self.isEmpty():
            return '[]'
        correntNo = self.primeiro
        string = '[' + str(correntNo.get_value())
        correntNo = correntNo.get_proximo()
        while correntNo.get_value() is not None:
            string += ", " + str(correntNo.get_value())
            
            correntNo = correntNo.get_proximo()
        string = string + ']'
        return string
    

    def adicionar(self,value):
        node = Nodulo(value,self.vazio)
        if self.isEmpty():
            self.primeiro = self.ultimo = node
        else:
            self.ultimo.set_proximo(node)
            self.ultimo = node
            
    def retirar(self):
        nodule = self.primeiro
        if nodule is self.ultimo:
            self.primeiro = self.ultimo = self.vazio
        elif nodule.get_proximo() is self.ultimo:
            self.primeiro = self.ultimo = nodule.get_proximo()
        else:
            self.primeiro = self.primeiro.get_proximo()
        return nodule.get_value()
                    

    def isEmpty(self):
        return self.primeiro is self.vazio

    
def achar_maior_caminho_possível(vertice_principal,N,caminhos):
    fila = L()
    inicio = vertice_principal
    distancias = [float('inf')]*N
    distancias[vertice_principal] = 0
    for a in caminhos[vertice_principal]:
        fila.adicionar(a)
        distancias[a[0]] = a[1]
    
    while not fila.isEmpty():
        vetor = fila.retirar()
        vertice = vetor[0]
        distancia_ate_vertice = vetor[1]

        if distancia_ate_vertice == distancias[vertice]:
            for a in caminhos[vertice]:
                if distancias[a[0]] > a[1] + distancia_ate_vertice:
                    distancias[a[0]] = a[1] + distancia_ate_vertice
                    fila.adicionar((a[0],a[1]+distancia_ate_vertice))
    maior = 0
    for a in distancias:
        if a != float('inf') and a != 0 and a > maior:
            maior = a


    return maior 


def main():

        N,M = map(lambda i: int(i),input().split(' '))
        grafo = [[] for a in range(N)]
        for a in range(M):
            U,V,P = map(lambda i: int(i),input().split())
            grafo[U].append((V,P))
            grafo[V].append((U,P))
        menor_possível = float('inf')

        for k in range(N):
            distancia = achar_maior_caminho_possível(k,N,grafo)
            if distancia< menor_possível:
                menor_possível = distancia

        return menor_possível
                

menor = main()


print(menor)
