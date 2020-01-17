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
    


def busca(valor,quantidade,i,j):
    global campo
    #Função recursivo para achar partes do navio, não foi utilzado por causa que dá RecursionError.
    campo[i][j] = valor
    quantidade += 1
    if campo[i-1][j] == None:
        quantidade = busca(valor,quantidade,i-1,j)
    if campo[i][j-1] == None:
        quantidade  = busca(valor,quantidade,i,j-1)
    if campo[i+1][j] == None:
        quantidade = busca(valor,quantidade,i+1,j)
    if campo[i][j+1] == None:
        quantidade = busca(valor,quantidade,i,j+1)
    return quantidade



N,M = map(lambda i: int(i),input().split(' '))
campo = []
for i in range(N+2):
    campo.append([0 for j in range(M+2)])

navios = []
valor = 1
for a in range(1,N+1):
    s = input()
    for p,b in enumerate(s):
        if b == '#':
            campo[a][p+1] = None


for a in range(1,N+1):
    for b in range(1,M+1):
        if campo[a][b] == None:
            queue = L()
            queue.adicionar((a,b))
            campo[a][b] = valor
            data = 0
            while not queue.isEmpty():
                coordenate = queue.retirar()
                i,j = coordenate[0],coordenate[1]
                data+=1
                if campo[i-1][j] == None:
                    queue.adicionar((i-1,j))
                    campo[i-1][j] = valor
                if campo[i][j-1] ==None:
                    queue.adicionar((i,j-1))
                    campo[i][j-1] = valor
                if campo[i+1][j] == None:
                    queue.adicionar((i+1,j))
                    campo[i+1][j] = valor
                if campo[i][j+1] == None:
                    queue.adicionar((i,j+1))
                    campo[i][j+1] = valor
            navios.append(data)
            valor +=1
K = int(input())
resultado = 0
for a in range(K):
    i,j = map(lambda i:int(i),input().split(' '))
    if campo[i][j]:
            navios[campo[i][j]-1] -=1
for a in navios:
    if a == 0:
        resultado +=1
                
print(resultado)
