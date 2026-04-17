frase = "Boa noite Turma de Ciência de Dados..."
print (frase[:9]) #Gera um "slice" da frase: range de 0 a 9, retorna a saída "Boa noite"
print (frase[10:15]) #Gera um "slice" da frase: range de 10 a 15, retorna a saída "Turma"
print (frase[::2]) #"slice" da frase: deixando o range aberto + incremento 2, ou seja, [0:0:2]
                   #ele pega um caracter, pula outro, pega, pula, etc
print (frase[::-1]) #"slice" da frase: deixando o range aberto + incremento (-1), ou seja, [0:0:-1]
                    #ele retorna a frase de tras pra frente (direita para esquerda)

