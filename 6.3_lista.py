filmes = ["Uma batalha após a outra", "MIB", "Godzilla"]

#Mostra toda a lista
print(filmes)
#Mostra o tipo da estrutura 
print(type(filmes))
#Mostra apenas o item (filme) que estou pedindo (0 mostra filme 1, 1 mostra filme 2, 2 mostra filme 3)
print(filmes[1])
#Mostra o último item da lista (utilizando o -, ele "navega" da direita pra esquerda)
print(filmes[-1])
#Adicionar um item na lista
filmes.append("Pecadores")
print(filmes[-1]) #Novamente solicitando o último, para ver se o filme "Pecadores" foi incluído
#Mostra toda a lista
print(filmes)
#Tamanho da lista
print(len(filmes))
#Recuperando o indice de um elemento pelo nome
print(filmes.index("Godzilla"))
#Ordena lista
filmes.sort()
print(filmes)
#Copia lista para outra
listaCopia = filmes.copy()
print(listaCopia)
#Invertendo
listaInvertida = sorted(filmes,reverse=True)
print(listaInvertida)
#Removendo
listaInvertida.remove("MIB")
print(listaInvertida)
#Remove todos os itens da lista
listaInvertida.clear()
print(listaInvertida)








