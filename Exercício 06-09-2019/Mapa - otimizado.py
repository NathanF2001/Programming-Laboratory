class Pintar_Mapa(object):

    def __init__(self):
        ''' ~Método Construtor~
        É estabelecido todos os vetores que serão utilizadas para pintar o mapa.
        '''
        self.provincias_vizinhas = [] #Lista dos adjacentes de cada uma das provincias.
        self.cores_vizinhas = {} #Dicionário que vai guarda as cores as quais a provincia não poderá pintar,sendo a ultima da lista sendo sua cor.
        self.provincias_pintadas = [] #Lista que dá referência das provincias que foram pintadas.
        self.main()
        


    def main(self):
        ''' ~Main
        Onde será executado todo algoritmo.
        '''
        self.quantidade_provincias = int(input("Digite o número de províncias: ")) # Entrada representando a quantidade de provincias.
        
        for t in range(self.quantidade_provincias): # Laço para pegar referência de adjacentes de cada provincia.
            dado = input('''Província %d:
Escreva quais províncias é adjacente a ela:
Separada por vírgulas(Ex: 1,2,5):'''%(t+1)).split(',')# Aqui será pegada os adjacentes de cada provincia, cada adjacente é separado pelo caractere ",".
            self.cores_vizinhas[t+1] = [] #Dicionário das cores as quais não pode ser pintada.
            self.provincias_vizinhas.append(dado)
        
        self.prioridade_provincia = self.ordernar_por_grau() # Cria uma lista que contém as provincias organizadas pelo seu grau de vertice.

        self.pintar_grupo_grafo() # Pintar o grafo

        cor_mínima = self.Cores_mínima() #Calcular aa cores mínimas


        print("O número mínimo é %d cores."%(cor_mínima+1))#Imprimir as cores mínimas


    def ordernar_por_grau(self):
        '''
        O grafo será organizado por grau do vértice pela ordem decrescente.
        '''
        return sorted(self.provincias_vizinhas,key = len,reverse= True)

    
    def pintar_grupo_grafo(self):
        '''
        Pintar todo o grafo.
        '''
    
        for p,z in enumerate(self.prioridade_provincia): #Laço na lista que foi ordenada pelo valor do grau,portanto o algoritmo passará por todos os vértices
            maior_grau = self.principal_provincia_a_pintar(p) # Pega o maior vértice de acordo com o laço

            
            if self.provincias_vizinhas.index(maior_grau) not in self.provincias_pintadas:# Checar se o vértice que está já está pintado
                self.pintar(self.provincias_vizinhas.index(maior_grau))
                
            proximo = self.provincia_secundaria_para_começar_a_pintar(maior_grau,self.provincias_vizinhas.index(maior_grau))#Próximo vértice a ser pintado.

            if proximo == None:
                continue
            else:
                self.pintar(proximo)
                referencia = self.provincias_vizinhas.index(maior_grau)
                while True:
                    proximo =  self.proximo_termo_do_grupo(proximo,referencia)#Procura um vertice que seja adjacente ao ultimo que foi pintado e que seja adjacente ao principal
                    if proximo == None:
                        proximo = self.Achar_outra_provincia(maior_grau)
                        if self.CheckList(maior_grau) is True: #Condição caso todos vertices adjacente ao principal seja pintados.
                            break
                    self.pintar(proximo)
                    


    def principal_provincia_a_pintar(self,i):
        '''
        Escolher o vértice que tem o maior grau sem contar aqueles que já foram referenciados nesse mesmo método.
        '''
        return self.prioridade_provincia[i]

    def provincia_secundaria_para_começar_a_pintar(self,provincia_maior_grau,p):
        '''
        Escolher a provincia que tem como referência a provincia principal.
        '''
        for k in provincia_maior_grau: #Laço para encontar a provincia dentro da provincia principal.
            if str(p+1) in self.provincias_vizinhas[int(k)-1] and int(k)-1 not in self.provincias_pintadas: #condição para que ela seja escolhida.
                return int(k)-1# retorna a sua posição em relação a lista de de adjacentes.
        return None# Caso a condição não seja satisfeita



    def pintar(self, index):
        '''
        Pintar os vértices.
        '''

        for c in range(5):# Laço baseado teorema das 4 cores
            if c not in self.cores_vizinhas[index+1]:# checa se a cor a qual vai pintar está dentro do dicionário de condições de cores do vértice.
                self.cores_vizinhas[index+1].append(c)
                if index not in self.provincias_pintadas:#Caso o vertice não esteja na lista que referencia os que ja foram pintados.
                    self.provincias_pintadas.append(index)
                for b in self.provincias_vizinhas[index]:# Colocar condição que os vizinhos ao vértice em questão não pode ter a cor que ele acabou de obter.
                    if int(b)-1 not in self.provincias_pintadas and c not in self.cores_vizinhas[int(b)]:
                        self.cores_vizinhas[int(b)].append(c)
                break
        return
            
    def proximo_termo_do_grupo(self,provincia,referencia):
        '''
        Achar próximo vértice que esteja relacionado a provincia principal.
        '''
        for k in self.provincias_vizinhas[provincia]:
            if str(referencia+1) in self.provincias_vizinhas[int(k)-1] and int(k)-1 not in self.provincias_pintadas:
                return int(k)-1
        return None

    def CheckList(self,array):
        '''
        Checar se todos adjacentes foram pintados.
        '''
        for a in array:
            if (int(a)-1) not in self.provincias_pintadas:
                return False

        return True

    def Cores_mínima(self):
        '''
        Fazer contagem de cores que foram utilizadas.
        '''
        minimo = 0
        for a in self.cores_vizinhas:
            if self.cores_vizinhas[a][-1] > minimo:
                minimo = self.cores_vizinhas[a][-1]
        return minimo
            
    def Achar_outra_provincia(self,array):
        '''
        Condição para achar outra provincia que não foi pintada e pertence a adjacência do vertice principal.
        '''
        for a in array:
            if (int(a)-1) not in self.provincias_pintadas:
                return int(a)-1
        


mapa = Pintar_Mapa()

