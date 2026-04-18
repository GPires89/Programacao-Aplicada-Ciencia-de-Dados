"""
Ler n palavras 
guardando-as numa lista
"""
palavra=[] #cria a lista palava[]

p = ""
i = 1
resposta="sim"
while resposta=="sim":

    while p!="fim":
        p = input(f"Informe a {i}ª palavra: ")
        if p!= "fim":
            palavra.append(p) #Adiciona palavras na lista

        #aqui está fora do if
        i+=1

    #aqui está fora do while
    print (palavra)  

    #Listar com numeração       
    for i, p in enumerate(palavra,start=1): #"i" é o índice e "p" é a palavra
        print(f"{i}ª palavra: {p}")

    palavra.sort() #ordena a lista em ordem alfabética

    print(palavra)

    resposta = input("Deseja continuar (sim/não:) ").lower()
