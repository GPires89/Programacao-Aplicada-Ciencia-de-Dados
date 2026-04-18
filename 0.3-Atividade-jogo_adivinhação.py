import random

def jogar():
    print("\n" + 35*"=")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
    print(35*"=")

    #VARIÁVEL: Armazena o número secreto gerado aleatoriamente
    numero_secreto = random.randint(1,100)

    #VARIÁVEL: Contador de tentativas
    tentativas = 0
    acertou = False

    #REPETIÇÃO: O bloco de código rodará enquanto o jogador não acertar
    while not acertou:
        chute = int(input("Tente adivinhar o número (1 a 100): "))
        tentativas += 1 #Incrementando a variável de repetição
    
        # DECISÃO: Verifica se o número é igual, maior ou menor
        if chute == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            acertou = True
            resposta = input ("Gostaria de jogar novamente? (sim/nao) ")
            if resposta == "sim":
                print("Então lá vamos nós novamente!!\n")
                jogar()
            else:
                print("Obrigado por jogar. Até a próxima.\n")
        elif chute < numero_secreto:
            print("O número secreto é MAIOR")
        else:
            print("O número secreto é MENOR")         

if __name__ == "__main__":
    jogar()