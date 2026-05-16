import os
import subprocess as spr
import time
import pprint

# --------------------------------------------------------------------------------------
#Função: cadastrar filme
# --------------------------------------------------------------------------------------
def cadastrar_filme():
    print("\nCadastrar Filme:")
    titulo = input("Digite o nome do Filme: ").strip()
    
    lancamento = int(input("Digite o ano de lançamento do filme: "))
    rating = float(input("Digite a avaliação do filme: "))
    
    generos = []
    print("\nInforme 3 generos de filme: ")
    for i in range(3):
        genero = input(f"Gênero {i+1}: ").strip()
        generos.append(genero)

    filme = {
        "Título": titulo,
        "Lançamento": lancamento,
        "Rating": rating,
        "Gênero": generos,
    }
    return filme

# --------------------------------------------------------------------------------------
#Função: listar filme
# --------------------------------------------------------------------------------------
def listar_filmes():
    print("="*80)
    print(f"{'Filme':<25} {'Lançamento':<12} {'Rating':<10} {'Gênero'}")
    print("="*80)
    for filme in filmesGeral.values():
        generos_formatados = ", ".join(filme['Gênero']) if isinstance(filme['Gênero'], list) else filme['Gênero']
        print(f"{filme['Título']:<25} {filme['Lançamento']:<12} {filme['Rating']:<10} {generos_formatados}")

# --------------------------------------------------------------------------------------
#Função: alterar filme
# --------------------------------------------------------------------------------------
def alterar_filme():
    titulo = input ("Digite o nome do filme que deseja alterar:")
    if titulo in filmesGeral:
        print("Filme encontrado, digite os novos dados:")
        filme = cadastrar_filme()
        filmesGeral[titulo] = filme
        print("Filme alterado com sucesso!")
    else:
        print("Filme não encontrado.")

# --------------------------------------------------------------------------------------
#Função: excluir filme
# --------------------------------------------------------------------------------------
def excluir_filmes():
    titulo = input ("Digite o nome do filme que deseja excluir:")
    if titulo in filmesGeral:
        del filmesGeral[titulo]
        print("Filme excluído com sucesso!")
    else:
        print("Filme não encontrado.")

# --------------------------------------------------------------------------------------
#Função: Gravar JSON
# --------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------
#Função: Imprimir JSON
# --------------------------------------------------------------------------------------




# --------------------------------------------------------------------------------------
#Criando variável para o dicionário aninhado
# --------------------------------------------------------------------------------------
filmesGeral = {}

# --------------------------------------------------------------------------------------
#Função principal (Menu)
# # --------------------------------------------------------------------------------------
while True:
    spr.run("cls", shell=True)#Limpa a tela
    print("="*21)
    print("**** Menu Filmes ****")
    print("="*21)
    print("1- Cadastrar Filmes")
    print("2- Listar Filmes")
    print("3- Alterar Filmes")
    print("4- Excluir Filmes")
    print("5- Gravar JSON")
    print("6- Imprimir JSON")
    print("0- Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        resposta = "s"
        while resposta.lower() in ("sim", "s"):
            os.system('cls')
            filme = cadastrar_filme()
            filmesGeral[filme["Título"]] = filme
            print("\nFilme inserido com sucesso!")
            resposta = input("\nDeseja continuar? (s/n)")
    elif opcao == "2":
        if len(filmesGeral) == 0:
            print("Nenhum filme cadastrado.")
        else:
            listar_filmes()
    elif opcao == "3":
        alterar_filme()
    elif opcao == "4":
        excluir_filmes()
    elif opcao == "0":
        break
    else:
        print("\n[***Opção inválida! Tente novamente]")
    time.sleep(5)

    

      
        
