import os

#Ler um número e dizer se ele é par ou impar

resposta="sim"
while resposta=="sim":
    #Entradas
    os.system('cls') #comando para limpar a tela
    x=int(input("Informe o valor de x: "))

    #Saídas
    if x%2==0:
        print("o número é par")
    else:
        print("O número é impar")
    resposta=input("Deseja continuar? (sim/não)")