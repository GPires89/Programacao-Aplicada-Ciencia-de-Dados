import pprint

filmesGeral = {
    "MIB": {
        "Lancamento": 2000,
        "Rating": 9.5,
        "genero": ["Ficção", "Suspenre", "Trilogia"]
    },
    "GATTACA":{
        "Lancamento": 1990,
        "Rating": 10.0,
        "genero": ["Ficção", "Suspense"]
    },
    "A vida é bela":{
        "Lancamento": 2019,
        "Rating": 9.0,
        "genero": ["Drama", "Guerra", "Crítica"]
    },
    "Os Incríveis":{
        "Lancamento": 2000,
        "Rating": 9.5,
        "genero": ["Ficção", "Suspenre", "Trilogia"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmesGeral)
print(len(filmesGeral))

#1 - Buscar uma informação dentro de um dicionário aninhado
print(filmesGeral["GATTACA"]["Lancamento"])

#2 - Adicionar novo ["[ item
filmesGeral["MIB"]["Diretor"] = "Steven Spielberg"
#pp.print(filmesGeral)
print(filmesGeral)

#3 - Excluir um dicionário
del filmesGeral["MIB"]

pp.pprint(filmesGeral)