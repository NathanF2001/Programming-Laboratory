def busca(fila,valor,data):
    global campo
    global navios
    i,j = fila.pop(0)
    data += 1
    campo[i][j] = valor
    if campo[i-1][j] == None:
        fila.append((i-1,j))
    if campo[i][j-1] ==None:
        fila.append((i,j-1))
    if campo[i+1][j] == None:
        fila.append((i+1,j))
    if campo[i][j+1] == None:
        fila.append((i,j+1))
    if fila != []:
        data = busca(fila,valor,data)
    return data
N,M = map(lambda i: int(i),input().split(' '))
campo = []
for i in range(N+2):
    campo.append([0 for j in range(M+2)])

navios = [0]
valor = 1
agua = True
for a in range(1,N+1):
    s = input()
    for p,b in enumerate(s):
        if b == '#':
            campo[a][p+1] = None
        elif agua:
            agua = False
if agua:
    partes = N*M
    K = int(input())
    resultado = -1
    for a in range(K):
        partes -=1
    if partes == 0:
        print(1)
else:
    for a in range(1,N+1):
        for b in range(1,M+1):
            if campo[a][b] == None:
                fila = [(a,b)]
                data = busca(fila,valor,0)
                navios.append(data)
                valor +=1
    K = int(input())
    resultado = -1
    for a in range(K):
        i,j = map(lambda i:int(i),input().split(' '))
        if campo[i][j]:
            navios[campo[i][j]] -=1
    for a in navios:
        if a == 0:
            resultado +=1
                
    print(resultado)
