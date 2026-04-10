import os

#Testando sequência lógica de atribuição de variáveis
"""
Este código lê dois números do tipo float representando base e altura
e calcula a área do triângulo
"""

resposta="sim"
while resposta=="sim":
    #Entradas
    os.system('cls') #comando para limpar a tela
    base=float(input("Informe o valor da base: "))
    altura=float(input("Informe o valor da altura: "))

    #Processamento
    area = base * altura / 2

    #Saídas
    print(f"A área do triângulo é {area}")
    resposta=input("Deseja continuar? (sim/não)")