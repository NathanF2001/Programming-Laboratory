class No():

    def __init__(self,caractere):
        self.caractere = caractere
        self.prox = None
        self.ant = None


    def getprox(self):
        return self.prox

    def getant(self):
        return self.ant

    def setprox(self,i):
        self.prox = i

    def setant(self,i):
        self.ant = i

class Pilha():

    def __init__(self):
        self._inicio = None
        self._fim = None

    def empilhar(self,novono):
        if self.EhVazio():
            self._inicio = self._fim = novono
        else:
            novono.setant(self._fim)
            self._fim.setprox(novono)
            self._fim = novono

    def desempilhar(self):
        if self.EhVazio():
            return None
        else:
            ultimo = self._fim
            if self._inicio == self._fim:
                self._inicio = self._fim = None
            else:
                penultimo = ultimo.getant()
                penultimo.setprox(None)
                self._fim = penultimo
                
            return ultimo.caractere

    def EhVazio(self):
        return self._fim == None

def transformar(string):
    if string == '}':
        return '{'
    elif string == ']':
        return '['
    else:
        return '('

instancias = int(input())

for a in range(instancias):
    cadeia = input()
    Validador = Pilha()
    valido = True
    for caractere in cadeia:
        if caractere == '(' or caractere == '[' or caractere == '{':
            no = No(caractere)
            Validador.empilhar(no)
        else:
            no = Validador.desempilhar()
            validar = transformar(caractere)
            if validar != no:
                valido = False
                break
    if not Validador.EhVazio():
        valido = False
    print('S') if valido else print('N')
                
                
        























        

    
