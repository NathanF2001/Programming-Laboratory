Passos = input("Digite a lista de comandos do robô: ").upper()
#Verificar se tem a string "TF" e a coloca como string vazia
while "TF" in Passos:
    Passos = Passos.replace("TF","")
#Verificar se tem a string "FT" e a coloca como string vazia
while "FT" in Passos:
    Passos = Passos.replace("FT","")
if len(Passos)>0:
    print("O robô deu %d passos em relação ao ponto inicial."%len(Passos)) #Aqui faz uma contagem de quantos passos ele deu direto para o percusso
else:
    print("O robô não saiu do lugar.") # Aqui mostra que o robô não teve taxa de variação entre o inicio e o fim

    
