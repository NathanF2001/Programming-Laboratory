Passos = input("Digite a lista de comandos do robô: ").upper()
while "TF" in Passos:
    Passos = Passos.replace("TF","")
while "FT" in Passos:
    Passos = Passos.replace("FT","")
print(Passos) #Aqui está os passos sem está sendo contado
if len(Passos)>0:
    print("O robô deu %d passos em relação ao ponto inicial."%len(Passos)) #Aqui faz uma contagem de quantos passos ele deu direto para o percusso
else:
    print("O robô não saiu do lugar.") # Aqui mostra que o robô não teve taxa de variação entre o inicio e o fim

    
