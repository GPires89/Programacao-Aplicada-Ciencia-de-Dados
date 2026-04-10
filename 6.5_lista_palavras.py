"""
Ler n palavras 
guardando-as numa lista
"""
palavra=[] #cria a lista palava[]

p = ""
i = 1
while p!="fim":
    p = input(f"Informe a {i}ª palavra: ")
    if p!= "fim":
        palavra.append(p)
    #aqui está fora do if
    i+=1
#aqui está fora do while
print (palavra)  
#Listar com numeração       
for i, p in enumerate(palavra,start=1):
    print(f"{i}ª = {p}")

print(palavra.sort())
