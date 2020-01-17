Numero_de_ponto = int(input())
pregos_horizontais = list(map(lambda i:int(i),input().split()))
total_de_cruzamentos = 0
for a in range(Numero_de_ponto):
    for b in range(a,-1,-1):
        if pregos_horizontais[a] < pregos_horizontais[b]:
            total_de_cruzamentos += 1

print(total_de_cruzamentos)
