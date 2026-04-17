#Gerando números com o for, apresentando-os como a tabuada

import os
resposta="sim"
while resposta=="sim" or resposta=="s":
    os.system("cls")
    n = int(input("Informe um número: "))
    print(f"Tabuada do nº {n}")
    print("="*20)
    for i in range(1,11):
        if i<=9:
            print(f"{n} x {i} = {n*i}")
        else:
            print(f"{n} x {i} = {n*i}")
            print("="*20)
    #aqui já estou fora do for
    resposta=input("\n\nDeseja ver mais tabuadas(sim/não)? ") .lower()
#aqui já estou fora do while 