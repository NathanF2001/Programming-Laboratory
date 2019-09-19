class Menor_caminho(object):

    def __init__(self):
        '''
            Método construtor que chama o método main.
        '''
        self.main()

    def main(self):
        '''
            Método que cria o grafo do mapa e os arranjos que serão utilizados no algoritmo.
        '''
        self.grafo()
        self.fila = [] 
        self.visitados = [0 for a in range(self.n)]
        
        z = self.achar_menor_caminho(self.inicio-1,self.fim-1)
        
    def achar_menor_caminho(self,inicio,final,quantidade = 0):
        '''
            Método do algoritmo.
        '''
        passado = str(inicio)
        while inicio != final:
            for a in self.grafo[inicio]:
                if self.visitados[a[0]] == 0:
                    t = self.Try_Change(a[0],quantidade+a[1])
                    if t:
                        self.fila[t] = [quantidade + a[1],a[0],passado + ','+ str(a[0])]
                    elif t == False:
                        self.fila.append([quantidade + a[1],a[0],passado + ','+ str(a[0])])
                        

            self.visitados[inicio] = 1
            index = min(self.fila, key=lambda x: x[0])
            self.fila.remove(index)
            quantidade,inicio,passado = index
            
        print('Percusso:\n')
        for p,a in enumerate(passado.split(',')):
            print(' -> ',end='') if p!= 0 else None
            print('Cidade %d '%(int(a)+1),end='')
        print('\n')
        return print('Menor distância: %d'%quantidade)
    

                    
                    
    def grafo(self):
        '''
            Método que cria o grafo.
        '''
        self.n,v,self.inicio,self.fim = map(lambda i: int(i), input().split(' '))
        self.grafo = [[] for a in range(self.n)]
        for a in range(v):
            c1,c2,d = map(lambda i: int(i), input().split(' '))
            self.grafo[c1-1].append((c2-1,d))
            self.grafo[c2-1].append((c1-1,d))
        
        return

    def Try_Change(self,i,k):
        '''
            Método que checa se o novo caminho até o vértice é menor no caminho que já está estabelecido.
        '''
        for p,a in enumerate(self.fila):
            if a[1] == i:
                if k< a[0]:
                    return p
                else:
                    return None
        return False


menorcaminho = Menor_caminho()



