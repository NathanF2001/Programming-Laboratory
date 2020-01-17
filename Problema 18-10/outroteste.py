class Node:

    def __init__(self,data,vertice,right = None,left = None,daddy = None,color = 'RED'):
        self.left = left
        self.data = data
        self.vertice = vertice
        self.right = right
        self.daddy = daddy
        self.color = color

    def consultar(self):
        if  self.getinfo() is None:
            return
        data = self.getinfo()
        left = self.left.getinfo()
        right = self.right.getinfo()
        print('Nodulo: ',data,'/','Left: ',left,'/'+'Right: ',right,'/'+'Cor: '+self.color)
        if right is not None:
            self.getright().consultar()
        if left is not None:
            self.getleft().consultar()


    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getinfo(self):
        return self.data

    def getfather(self):
        return self.daddy

    def setleft(self,i):
        self.left = i

    def setright(self,i):
        self.right = i

    def setinfo(self,i):
        self.data = i

    def setfather(self,i):
        self.daddy = i


class Binary_tree:

    def __init__(self):
        self.vazio = Node(None,None,color = 'BLACK')
        self.vazio.setfather(self.vazio)
        self.vazio.setright(self.vazio)
        self.vazio.setleft(self.vazio)
        self.root = self.vazio

                           
    def RB_insert(self,i):
        nodulo = Node(i[1],i[0],self.vazio,self.vazio,self.vazio)
        x = self.root
        y = self.vazio
        while x != self.vazio:
            y = x
            if i[1] < x.getinfo():
                x = x.getleft()
            else:
                x = x.getright()
        nodulo.setfather(y)
        if y == self.vazio:
            self.root = nodulo
        else:
            if i[1] < y.getinfo():
                y.setleft(nodulo)
            else:
                y.setright(nodulo)
        self.RB_insert_fixup(nodulo)

    def add(self,i,cor):
        nodulo = Node(i,self.vazio,self.vazio,self.vazio,color = cor)
        x = self.root
        y = self.vazio
        while x != self.vazio:
            y = x
            if i < x.getinfo():
                x = x.getleft()
            else:
                x = x.getright()
        nodulo.setfather(y)
        if y == self.vazio:
            self.root = nodulo
        else:
            if i < y.getinfo():
                y.setleft(nodulo)
            else:
                y.setright(nodulo)

    def RB_insert_fixup(self,z):
        while z.getfather().color == 'RED':
            if self.isleft(z.getfather()):
                y = z.getfather().getfather().getright()
                if y.color == 'RED':
                    z.getfather().color = 'BLACK'
                    y.color = 'BLACK'
                    z.getfather().getfather().color = 'RED'
                    z = z.getfather().getfather()
                else:
                    if self.isright(z):
                        z = z.getfather()
                        self.left_rotate(z)
                    z.getfather().color = 'BLACK'
                    z.getfather().getfather().color = 'RED'
                    self.right_rotate(z.getfather().getfather())
            else:
                y = z.getfather().getfather().getleft()
                if y.color == 'RED':
                    z.getfather().color = 'BLACK'
                    y.color = 'BLACK'
                    z.getfather().getfather().color = 'RED'
                    z = z.getfather().getfather()
                else:
                    if self.isright(z):
                        z = z.getfather()
                        self.right_rotate(z)
                    z.getfather().color = 'BLACK'
                    z.getfather().getfather().color = 'RED'
                    self.left_rotate(z.getfather().getfather())
        self.root.color = 'BLACK'
        
    def RB_delete(self,nodule): 
        if nodule.getleft() is self.vazio or nodule.getright() is self.vazio:
            y = nodule
        else:
            y = self.tree_successor(nodule)
        if y.getleft() is not self.vazio:
            x = y.getleft()
        else:
            x = y.getright()
        if x is not self.vazio:
            x.setfather(y.getfather())
        if y.getfather() is self.vazio:
            self.root = x
        else:
            if y == y.getfather().getleft():
                y.getfather().setleft(x)
            else:
                y.getfather().setright(x)

        if y != nodule:
            nodule.setinfo(y.getinfo())
        if y.color == 'BLACK':
            self.RB_DELETE_FIXUP(x)
    
        return y

    def RB_DELETE_FIXUP(self,x):
        while x != self.root and x.color == 'BLACK':
            if self.isleft(x):
                w = x.getfather().getright()
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.getfather().color = 'RED'
                    self.left_rotate(x.getfather())
                    w = x.getfather().getright()
                if w.getleft().color =='BLACK' and w.getright().color == 'BLACK':
                    w.color = 'RED'
                    x = x.getfather()
                else:
                    if w.getright().color == 'BLACK':
                        w.getleft().color = 'BLACK'
                        w.color = 'RED'
                        self.right_rotate(w)
                        w = x.getfather().getright()
                        w.color = x.getfather().color
                        x.getfather().color = 'BLACK'
                        w.getright().color = 'BLACK'
                        self.left_rotate(x.getfather())
                        x = self.root
            else:
                w = x.getfather().getleft()
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.getfather().color = 'RED'
                    self.right_rotate(x.getfather())
                    w = x.getfather().getleft()
                if w.getright().color =='BLACK' and w.getleft().color == 'BLACK':
                    w.color = 'RED'
                    x = x.getfather()
                else:
                    if w.getleft().color == 'BLACK':
                        w.getright().color = 'BLACK'
                        w.color = 'RED'
                        self.left_rotate(w)
                        w = x.getfather().getleft()
                        w.color = x.getfather().color
                        x.getfather().color = 'BLACK'
                        w.getright().color = 'BLACK'
                        self.right_rotate(x.getfather())
                        x = self.root
        x.color = 'BLACK'
    def isleft(self,nodule):
        q = nodule.getfather()
        if q == self.vazio:
            return False
        if q.getleft() is nodule:
            return True
        return False

    def isright(self,nodule):
        q = nodule.getfather()
        if q == None:
            return False
        if q.getright() is nodule:
            return True
        return False

    def tree_search(self,i):
        nodule = self.root
        while nodule.getinfo() is not None and i != nodule.getinfo(): 
            if i < nodule.getinfo():
                nodule = nodule.getleft()
            else:
                nodule = nodule.getright()
        return nodule
            
    def tree_minimum(self,nodule):
        while nodule.getleft() is not self.vazio:
            nodule = nodule.getleft()
        return nodule

    def tree_maximum(self,nodule):
        while nodule.getright() is not self.vazio:
            nodule = nodule.getright()
        return nodule

    def tree_successor(self,nodule):
        if nodule.getright() is not None:
            return self.tree_minimum(nodule.getright())
        y = nodule.getfather()
        while y != None and self == y.getright():
            x = y
            y = y.getfather()
        return y

    def tree_predecessor(self,nodule):
        if nodule.getleft() is not None:
            return self.tree_maximum(nodule.getleft())
        y = nodule.getfather()
        while y != None and self == y.getleft():
            x = y
            y = y.getfather()
        return y

    def tree_delete(self,z):
        nodule = self.tree_search(z)
        if nodule.getleft() is self.vazio or nodule.getright() is self.vazio:
            y = nodule
        else:
            y = self.tree_successor(nodule)
        if y.getleft() is not self.vazio:
            x = y.getleft()
        else:
            x = y.getright()
        if x is not self.vazio:
            x.setfather(y.getfather())
        if y.getfather() is self.vazio:
            self.root = x
        else:
            if y == y.getfather().getleft():
                y.getfather().setleft(x)
            else:
                y.getfather().setright(x)

        if y != z:
            nodule.setinfo(y.getinfo())
        return y

    def consultar_tree(self):
        self.root.consultar()



    def altura(self,nodule):
        if nodule == self.vazio:
            return -1
        h1 = self.altura(nodule.getleft())
        h2 = self.altura(nodule.getright())
        return (1+max(h1,h2))

    def AVL(self,nodule):
        if nodule == self.vazio:
            return -1,0
        h1,avl_e = self.AVL(nodule.getleft())
        h2,avl_d= self.AVL(nodule.getright())
        main_avl = h2-h1
        if -1<main_avl>1:
            if main_avl> 0:
                if avl_d<0:
                    self.right_rotate(nodule.getright())
                    self.left_rotate(nodule)
                else:
                    self.left_rotate(nodule)
            else:
                if avl_e>0:
                    self.left_rotate(nodule.getleft())
                    self.right_rotate(nodule)
                else:
                    self.right_rotate(nodule)
            h1 = self.altura(nodule.getleft())
            h2= self.altura(nodule.getright())
    
        return (1+max(h1,h2)),h2-h1


    def left_rotate(self,x):
        y = x.getright()
        x.setright(y.left)
        if y.getleft() != self.vazio:
            y.getleft().setfather(x)
        y.setfather(x.getfather())
        if x.getfather() == self.vazio:
            self.root = y
        else:
            if self.isleft(x):
                x.getfather().setleft(y)
            else:   
                x.getfather().setright(y)
        y.setleft(x)
        x.setfather(y)

    def right_rotate(self,x):
        y = x.getleft()
        x.setleft(y.right)
        if y.getright() != self.vazio:
            y.right.setfather(x)
        y.setfather(x.getfather())
        if x.getfather() == self.vazio:
            self.root = y
        else:
            if self.isright(x):
                x.getfather().setright(y)
            else:   
                x.getfather().setleft(y)
        y.setright(x)
        x.setfather(y)

def achar_maior_e_menor_caminho(vertice_principal,N,caminhos):
    fila = Binary_tree()
    inicio = vertice_principal
    distancias = [float('inf')]*N
    distancias[vertice_principal] = 0
    for a in caminhos[vertice_principal]:
        fila.RB_insert(a)
        distancias[a[0]] = a[1]
    
    while fila.root is not fila.vazio:
        node = fila.tree_minimum(fila.root)
        vetor = fila.RB_delete(node)
        vertice = vetor.vertice
        distancia_ate_vertice = vetor.data
        if distancia_ate_vertice == distancias[vertice]:
            for a in caminhos[vertice]:
                if distancias[a[0]] > a[1] + distancia_ate_vertice:
                    distancias[a[0]] = a[1] + distancia_ate_vertice
                    fila.RB_insert((a[0],a[1]+distancia_ate_vertice))
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
            distancia = achar_maior_e_menor_caminho(k,N,grafo)
            if distancia< menor_possível:
                menor_possível = distancia

        return menor_possível
                

menor = main()


print(menor)

                    
                    
