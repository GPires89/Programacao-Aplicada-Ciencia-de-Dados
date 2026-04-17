import os

#Classifica fase da vida

"""
Este código lê uma idade e informa a fase da vida
"Bebê", quando a idade for menor ou igual a 2
"Criança", quando a idade for menor ou igual a 10
"Pré adolescente", menor que 15
"Adolescente", menor que 18
"Jovem", menor ou igual a 30
"Adulto", menor que 60
"Melhor idade", maior ou igual a 60
"""

resposta="sim"
while resposta=="sim":
    #Entradas
    idade=int(input("informe o valor idade: "))

    #Saídas
    if idade<=2:
        print("Bebê")
    elif idade <=10:
        print("Criança")
    elif idade <15:
        print("Pré adolescente")
    elif idade<18:
        print("Adolescente")
    elif idade<=30:
        print("Jovem")
    elif idade<60:
        print("Adulto")
    else:
        print("Melhor idade")
    resposta=input("Deseja continuar? (sim/não)")