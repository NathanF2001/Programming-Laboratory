def Cores_mapa():
    global ordem
    global provincias_vizinhas
    global preenchida

    #O maior representa as cores, que está de acordo com o teorema das 4 cores, portanto so pode haverno máximo 4 cores.
    maior = 0
    

    #Um Arranjo representado as provincias já pintadas
    pintado = []

    #Utilizar o Arranjo ordem para começar a pintar cada província.
    for p,t in enumerate(ordem):
        #Esse laço representa as cores
        for a in range(4):
            #Aqui é checado se a cor ja está em uma província vizinha. Se for Falso, essa cor é dada a província atual.
            if str(a) not in preenchida[provincias_vizinhas.index(t)+1]:
                preenchida[provincias_vizinhas.index(t)+1] =  str(a)
                pintado.append(provincias_vizinhas.index(t)+1)
                break
        #Aqui pega a cor a qual foi pintada a província atual e coloca a condição para que suas vizinhas não tenha a mesmo cor.Isso é utilizado por meio do dicionário
        #'preenchida'.
        for b in t.split(','):
            if str(a) not in preenchida[int(b)] and (int(b) not in pintado):
                preenchida[int(b)] = preenchida[int(b)] + '/' + str(a)
        if a > maior:
            maior = a
            if maior == 3:
                break

    return maior

Pv = int(input("Digite o número de províncias: "))

#Arranjo que vai guardar as posições que são vizinhas
provincias_vizinhas = []
#Dicionário que vai guardar as cores que tem vizinha a cada província
preenchida = {}


#Adicionar as províncias vizinhas ao arranjo provincias_vizinhas
for t in range(0,Pv):
    dado = input("""Província %d:
Escreva quais províncias é adjacente a ela:
Separa por vírgulas(Ex: 1,2,5):
"""%(t+1))
    provincias_vizinhas.append(dado)
    preenchida[t+1] = ''

'''Criar um Arranjo de forma ordenada pelo tamanho dos Subarranjos de provincias_vizinhas. Pois é considerado que para colorir tem que ser do termo que tem mais
provincias congruentes.'''
ordem = sorted(provincias_vizinhas,key = len,reverse= True)

n1 = Cores_mapa()

print("O numero mínimo é %d cores"%(n1+1))


