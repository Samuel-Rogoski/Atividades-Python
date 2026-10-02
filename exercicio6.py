notas = {"Ana": 8.5, "Pedro": 6.0, "Maria": 9.0, "João": 5.5}

soma_notas = 0

for nota in notas.values():
    soma_notas += nota

media_geral = soma_notas / len(notas)

print(f"A média geral da turma é: {media_geral:.2f}")
