#Gerando números com o for
import os

resposta="sim"
while resposta=="sim":
    os.system("cls")
    for i in range(2,22,2):
        if i<=19:
            print(f"{i}, ", end="")
        else:
            print(f"{i}. ", end="")
    resposta = input("\n Deseja continuar? (sim/não): ").lower()
