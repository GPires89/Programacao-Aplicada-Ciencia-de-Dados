import os

#Ler dois numeros inteiros e informar qual é o maior ou se são iguais

"""
Ex: 
Se forem informados os números 56 e 78, a saída será:
78 é o maior
Se forem informados os números 10 e 10, a saída será:
Os números são iguais
"""

resposta="sim"
while resposta=="sim":
    #Entradas
    os.system('cls') #comando para limpar a tela
    x=int(input("Informe o valor de x: "))
    y=int(input("Informe o valor da y: "))

    #Saídas
    if x>y:
        print(f"{x} é o maior")
    elif x<y:
        print(f"{y} é o maior")
    else:
        print("Os números são iguais")
    resposta=input("Deseja continuar? (sim/não)")


