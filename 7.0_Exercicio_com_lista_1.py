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

os.system('cls')
listaNum = [] #lista vazia
n=0
i=1
NumPar = 0
NumImpar = 0
Soma = 0

while n!=-999:
    n=int(input(f"Informe o {i}º número: "))
    if n!=-999:
        listaNum.append(n)
        Soma= Soma + n
    i+=1
print(listaNum)
for i in range(0,len(listaNum)):
    if listaNum[i]%2==0:
        NumPar+=1
    if listaNum[i]%2==1:
        NumImpar+=1
        
    print(f"{i+1}º número: {listaNum[i]}")
traco("*",50) #equivale a print("*"*50)
print(f"Foram informados {len(listaNum)} nºs.")
traco("=",50) #equivale a print("="*50)
print(f"Foram informados {NumPar} nºs pares.")
traco("*",50) #equivale a print("*"*50)
print(f"Foram informados {NumImpar} nºs Impares.")
traco("=",50) #equivale a print("="*50)
print(f"A somatória dos números é {Soma}.")
traco("*",50) #equivale a print("*"*50)

    

