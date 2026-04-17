import random

def jogar():
    print("-----------------------------------------------")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
    print("-----------------------------------------------")

    #VARIÁVEL: armazena o número secreto gerado aleatoriamente
    numero_secreto = random.randint(1,100)

    #VARIÁVEL: contador de tentativas
    tentativas = 0
    acertou = False

    #REPETIÇÃO: O bloco de código rodará enquanto o jogador não acertar
    while not acertou:
        chute = int(input("Tente adivinhar o número (1 a 100): "))
        tentativas += 1 #Incrementando a variável de repetição

        # DECISÃO: Verifica se o número é igual, maior ou menor
        if chute == numero_secreto:
            print("Parabéns! Você acertou em {tentativas}.")
            acertou = True
        elif chute < numero_secreto:
            print("O número secreto é MAIOR")
        else:
            print("O número secreto é MENOR")

if __name__ == "__main__":
    jogar()





