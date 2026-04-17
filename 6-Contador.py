#Apenas exemplo: variável nome é str (string)
#nome = "Fernando" 

#Apenas para entender o conceito de atribuição de texto a uma variável que até então seria
#numeral inteiro, pedindo ao usuário que entre com a informação solicitada
#idade=int("digite sua idade: ") 

nome = input("Qual é o seu  nome: ")
print (f"Olá {nome}.")
valor_inicial = int(input("Valor inicial: "))
i = valor_inicial #Variável i é int
valor_final = int(input("Valor final: "))

while i<=valor_final:
    print(f"{i}, ", end="")
    i+=1

