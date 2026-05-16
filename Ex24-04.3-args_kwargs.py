def resumo_aluno(nome, *notas, **informacoes):
    print(f"Aluno: {nome}")

    if notas:
        media = sum(notas) / len(notas)
        print(f"Notas: {notas}")
        print(f"Media: {media:.2f}")
    else:
        print("Nenhuma nota informada.")

    if informacoes:
        print("Informacoes extras:")
        for chave, valor in informacoes.items():
            print(f"- {chave}: {valor}")
    else:
        print("Nenhuma informacao extra informada.")


resumo_aluno(
    "Gabriel",
    8.5,
    9.0,
    7.5,
    curso="Python",
    turma="Fundamentos",
    status="Aprovado"
)

print()

resumo_aluno("Ana", 10, 9.5, curso="Python")

print()

resumo_aluno("Carlos")
