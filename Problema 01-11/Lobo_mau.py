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

R,C = map(lambda i: int(i),input().split(' '))
matriz = []
for a in range(R):
    T= input()
    submatriz = []
    for b in T:
        if b == '.':
            submatriz.append(None)
        elif b == '#':
            submatriz.append(0)
        elif b == 'v':
            submatriz.append(1)
        else:
            submatriz.append(2)
    matriz.append(submatriz)
total_ovelhas = 0
total_lobos = 0
for a in range(R):
    for b in range(C):
        if matriz[a][b]:
            ovelhas = 0
            lobos = 0
            Queue = L()
            Queue.adicionar((a,b))
            if matriz[a][b] == 1:
                lobos += 1
            elif matriz[a][b] == 2:
                ovelhas += 1
            matriz[a][b] = 0
            while not Queue.isEmpty():
                index = Queue.retirar()
                i,j = index[0],index[1]
                if i-1>=0 and matriz[i-1][j] != 0:
                    Queue.adicionar((i-1,j))
                    if matriz[i-1][j] == 1:
                        lobos += 1
                    elif matriz[i-1][j] == 2:
                        ovelhas += 1
                    matriz[i-1][j] = 0
                if j-1>=0 and matriz[i][j-1] != 0:
                    Queue.adicionar((i,j-1))
                    if matriz[i][j-1] == 1:
                        lobos += 1
                    elif matriz[i][j-1] == 2:
                        ovelhas += 1
                    matriz[i][j-1] = 0
                if i+1<R and matriz[i+1][j] != 0:
                    Queue.adicionar((i+1,j))
                    if matriz[i+1][j] == 1:
                        lobos += 1
                    elif matriz[i+1][j] == 2:
                        ovelhas += 1
                    matriz[i+1][j] = 0
                if j+1<C and matriz[i][j+1] != 0:
                    Queue.adicionar((i,j+1))
                    if matriz[i][j+1] == 1:
                        lobos += 1
                    elif matriz[i][j+1] == 2:
                        ovelhas += 1
                    matriz[i][j+1] = 0
            if ovelhas > lobos:
                total_ovelhas += ovelhas
            else:
                total_lobos += lobos

print(total_ovelhas,total_lobos)
                    
