filme={
    "Titulo": "MIB",
    "Lancamento": 2000,
    "Rating": 9.5,
    "genero": ["Ficção", "Suspente", "Trilogia"]
}
print(filme)
print(len(filme))
print(type(filme))

#1 - Recuperar um elemento do dicionário

print(filme["genero"])
print(filme.get("Rating"))

#2 - Buscar apenas as chaves do dicionário
print(filme.keys())
#3 - Buscar apenas os valores do dicionário
print(filme.keys())
#4 - Buscar itens do dicionário com chave e valor
print(filme.items())
#5 - Adicionar um item do dicionário
filme["Diretor"]="Christopher Nolan"
print(filme)
#6 - Atualizar itens no dicionário
filme.update({"Rating": 10.0})
7# - Remover item do dicionário
filme.pop("Diretor")
print(filme)

