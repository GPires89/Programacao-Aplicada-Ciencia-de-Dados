""" 
    Receber do usuário uma lista de números.
    Finalizar a entrada quando for digitado -999.
    Descobrir quantos foram informados.
    Mostrar os seguintes resultados (saídas):

    - Foram informados ___ números pares    
    - Foram informados ___ números ímpares
    - A somatória dos números é ___
    - O Maior número foi o ___ na posição ___
    - O Menor número foi o ___ na posição ___
    - A média aritmética entre eles foi ___
"""
import os

def traco(caracter,qtd):
    print(caracter*qtd)

# Inicializamos a resposta para entrar no loop
resposta="sim"

while resposta=="sim" or resposta=="s":
    os.system('cls')

    numeros=[] #lista vazia
    n=0
    i=1
    Soma=0

    while n!=-999:
        n=int(input(f"Informe o {i}º número: "))
        if n!=-999:
            numeros.append(n)
            i+=1

    print(numeros)
    
    maior = max(numeros)
    menor = min(numeros)

    contPar = 0
    contImpar = 0

    for i in range(0,len(numeros)):
        if numeros[i]%2==0:
            contPar+=1
        else:
            contImpar+=1

        print(f"{i+1}º número: {numeros[i]}")
        Soma += numeros[i]

    traco("*",50) #equivale a print("*"*50)
    print(f"Foram informados {len(numeros)} nºs.")
    traco("=",50) #equivale a print("="*50)
    print(f"Foram informados {contPar} nºs pares.")
    traco("*",50) 
    print(f"Foram informados {contImpar} nºs Impares.")
    traco("=",50) 
    print(f"A somatória dos números é {Soma}.")
    traco("*",50) 
    print(f"O maior número foi o {maior} e estava na posição {numeros.index(maior) + 1}")
    traco("=",50) 
    print(f"O menor número foi o {menor} e estava na posição {numeros.index(menor) + 1}")
    traco("*",50) 
    print(f"A média aritmética dos números é: {(Soma/len(numeros)):.2f}")
    traco("=",50) 

    resposta = input("\nDeseja continuar? (s/n)")
