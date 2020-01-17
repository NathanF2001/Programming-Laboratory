class No():

    def __init__(self,nome,prioridade,gravidade):
        self.nome = nome
        self.prio = prioridade
        self.grav = gravidade
        self.prox = None

    def getnome(self):
        return self.nome

    def getprio(self):
        return self.prio

    def getgrav(self):
        return self.grav

    def getprox(self):
        return self.prox

    def setnome(self,i):
        self.nome = i

    def setprio(self,i):
        self.prio = i

    def setgrav(self,i):
        self.grav = i

    def setprox(self,i):
        self.prox = i

class Fila():

    def __init__(self):
        self._inicio = None

    def InserirNaFila(self,novono):
        if self._inicio == None:
            self._inicio = novono
        else:
            prioridade_do_no = novono.getprio()
            
            
            no_atual,anterior = self.PosicionarPrioridade(prioridade_do_no,self._inicio)
            
            if no_atual != None and no_atual.getprio() == prioridade_do_no:#Prioridade iguais, coloca prioridade agora a gravidade
                
                gravidade_do_no = novono.getgrav()
                no_atual,anterior = self.PosicionarGravidade(prioridade_do_no,gravidade_do_no,no_atual,anterior)
                
                if no_atual != None and no_atual.getgrav() == gravidade_do_no:#Gravidades iguais, coloca prioridade agora em relação ao nome

                    nome_do_no = novono.getnome()
                    no_atual,anterior = self.PosicionarNome(prioridade_do_no,gravidade_do_no,nome_do_no,no_atual,anterior)
                        
            novono.setprox(no_atual)
            if anterior != None:
                anterior.setprox(novono)
            if no_atual == self._inicio:
                self._inicio = novono

    def PosicionarPrioridade(self,prioridade,no):#Caso a prioridade do nó atual seja superior ao nó que queira inserir
        no_atual = no
        anterior = None
        while no_atual != None and no_atual.getprio() > prioridade:
            anterior = no_atual
            no_atual = no_atual.getprox()
        return no_atual,anterior

    def PosicionarGravidade(self,prioridade,gravidade,no,antecessor):#Caso a gravidade do nó atual seja superior ao nó que queira inserir
        no_atual = no
        anterior = antecessor
        while no_atual != None and no_atual.getprio() == prioridade and no_atual.getgrav() > gravidade:
            anterior = no_atual
            no_atual = no_atual.getprox()
        return no_atual,anterior

    def PosicionarNome(self,prioridade,gravidade,nome,no,antecessor):#Caso o nome do nó atual seja ,em ordem alfabetica, maior ao nó que queira inserir
        no_atual = no
        anterior = antecessor
        
        while no_atual != None and no_atual.getprio() == prioridade and no_atual.getgrav() == gravidade and no_atual.getnome() < nome:
            anterior = no_atual
            no_atual = no_atual.getprox()

        return no_atual,anterior
        

    def ImprimirPacientes(self):
        no_atual = self._inicio
        while no_atual != None:
            print(no_atual.getnome())
            no_atual = no_atual.getprox()

def IntPrioridade(string):
    if string == 'resto':
        return 1
    elif string == 'bronze':
        return 2
    elif string == 'prata':
        return 3
    elif string == 'ouro':
        return 4
    elif string == 'diamante':
        return 5
    else:
        return 6

pacientes = int(input())
Queue = Fila()
for a in range(pacientes):
    nome,prioridade,gravidade = input().split()
    prioridade = IntPrioridade(prioridade)
    gravidade = int(gravidade)
    paciente = No(nome,prioridade,gravidade)
    Queue.InserirNaFila(paciente)

Queue.ImprimirPacientes()



















        

    
