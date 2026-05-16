#1 - Imprime um nome completo 
def imprime_nome(pnome,psobrenome):
    print(f" *** {pnome} {psobrenome} ***")

imprime_nome("Anderson", "Amaral")

#2 - Função para somar dois números
def soma_dois(p1,p2):
    r= p1 + p2
    return r

n1 = 10
n2 = 15
print(f" {n1} + {n2} = {soma_dois(n1,n2)}")

#3 - Função com parâmetro e valor default
def endereco(pais="Brasil"):
    print(f"Eu moro em: {pais}")

endereco("Uruguai")
