class Heap_Sort(object):
    def __init__(self,Array):
        '''
            Algoritmo Heap Sort
        '''
        self.Array = Array
        self.size_heap = len(self.Array)-1
        self.Build_max_heap()
        
        for i in range(self.size_heap,0,-1):
            self.Array[0],self.Array[i] = self.Array[i],self.Array[0]
            self.size_heap = self.size_heap -1
            self.Max_heapify(0)

            
    def Build_max_heap(self):
        for i in range(self.size_heap//2,-1,-1):
            self.Max_heapify(i)

    def Max_heapify(self,i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.size_heap and self.Array[l][1] > self.Array[i][1]:
            maior = l
        else:   
            maior = i
        if  r <= self.size_heap and self.Array[r][1] > self.Array[maior][1]:
            maior = r
        if maior != i:
            self.Array[i],self.Array[maior] = self.Array[maior],self.Array[i]
            self.Max_heapify(maior)


    def parent(self,i):
        return i//2

    def left(self,i):
        return 2*i+1

    def right(self,i):
        return 2*i+2
    



N = int(input())#Número de colunas
array = list(map(lambda x: int(x),input().split(' ')))#Alturas das colunas
lista = []#Lista que vai guardar as colunas que são picos e vales.
for p,a in enumerate(array):
    if p == 0:#Caso seja primeira coluna
        if a > array[p+1]:#Se a próxima coluna for menor que a primeira coluna
            lista.append(('T',a))
    elif p == len(array)-1:#Caso seja a última coluna
        if a > array[p-1]:#Se a coluna anterior for menor que a ultima coluna
            lista.append(('T',a))
    else:
        if array[p-1]>=a<=array[p+1] and lista[-1] != a:#Se a coluna for menor que as vizinhas
            lista.append(('P',a))
        elif array[p-1]<=a>=array[p+1] and lista[-1] != a:#Se a coluna for maior que as vizinhas
            lista.append(('T',a))

Heap_Sort(lista)#Ordenar a lista
corte = 0 #Número de cortes
maior = 0 #Guardar o maior número de cortes possível
for a in lista:
    if a[0] == 'P':
        corte +=1
        if corte > maior:
            maior = corte
    else:
        corte -=1
print(maior+2)
