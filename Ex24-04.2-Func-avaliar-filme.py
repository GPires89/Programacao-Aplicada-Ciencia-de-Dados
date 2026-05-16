#1 Função para avaliar um filme
def avaliar_filme(pfilme,pqtd):
    print(f"Avaliação do filme {pfilme}")
    total=0
    for i in range(1,pqtd+1):
        avaliacao = int(input(f"Digite a {i} nota: "))
        total += avaliacao
    
    if pqtd>0:
        media = total/pqtd
    else:
        media = 0

    print(f"A média de avaliações do filme {pfilme} = {media:.2f}")

avaliar_filme("MIB", 4)

    