import random

# VARIÁVEL GLOBAL: O recorde fica fora da função para não ser resetado
recorde = None

def jogar():
    global recorde # Avisamos o Python que vamos usar a variável lá de fora

    print("\n" + 35*"=")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
    print(35*"=")

    #VARIÁVEL: Armazena o número secreto gerado aleatoriamente
    numero_secreto = random.randint(1,100)

    tentativas = 0  #VARIÁVEL: Contador de tentativas
    pontos = 1000 #VARIÁVEL: Pontuação inicial
    acertou = False

    #REPETIÇÃO: O bloco de código rodará enquanto o jogador não acertar
    while not acertou:
        print(f"Pontuação atual: {pontos}")
        chute = int(input("Tente adivinhar o número (1 a 100): "))
        tentativas += 1 #Incrementando a variável de repetição
    
        # DECISÃO: Verifica se o número é igual, maior ou menor
        if chute == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            print(f"Sua pontuação final: {pontos}")

            # DECISÃO: Verificar se é um novo recorde
            if recorde is None or tentativas < recorde:
                recorde = tentativas
                print("🏆 NOVO RECORDE ESTABELECIDO! 🏆")

            acertou = True
            resposta = input ("Gostaria de jogar novamente? (sim/nao) ")
            
            if resposta == "sim":
                print("Então lá vamos nós novamente!!\n")
                if recorde is not None:
                    print(f"Recorde atual: {recorde} tentativas.")
                jogar()
            
            else:
                print("Obrigado por jogar. Até a próxima.\n")
        
        elif chute < numero_secreto:
            print("O número secreto é MAIOR")
            pontos -= 100 # Subtração de pontos
        
        else:
            print("O número secreto é MENOR")
            pontos -= 100 # Subtração de pontos

        # DECISÃO: Se os pontos acabarem, o jogador perde
        if pontos <= 0:
            print(f"\nGame Over! Os pontos acabaram. O número era {numero_secreto}.")
            break #Interrompe a REPETIÇÃO (while)         

if __name__ == "__main__":
    jogar()