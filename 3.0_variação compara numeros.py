import os

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    x = int(input ("informe o valor de x: "))
    y = int(input ("informe o valor de y: "))

    if x==y:
        print('os números são iguais')
    else:
        print(f"{max(x,y)} é o maior")
    
    resposta = input('Deseja continuar? (sim/nao): ') .lower()

    if resposta !='sim':
        break
