#Aula 1
print("Diogo Silva")
print ("Boa noite")
# Atribuição
b = 10
a = 5
r = a + b

# Comando
print (a)
print (r)

#Exemplo
nome = input ("Qual o seu nome? ")
resposta = input ("Quer continuar conversa(sim/não) ") 
print (f" Boa noite {nome}, tudo bem?")
if resposta == "sim":
    print("Vamos continuar então...")
elif resposta == "não":
    print ("Até a próxima!")
else: 
    print("resposta invalida")