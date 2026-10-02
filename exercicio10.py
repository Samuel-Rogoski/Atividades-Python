boletim = {}

while True:
    opcao = input("Deseja adicionar um aluno? (sim/nao): ").strip().lower()
    
    if opcao == 'sim':
        nome = input("Digite o nome do aluno: ").strip()
        nota = float(input(f"Digite a nota de {nome}: "))
        boletim[nome] = nota
    elif opcao == 'nao':
        
        break
    else:
        print("Opção inválida! Digite 'sim' ou 'nao'.")

print("\n--- RESULTADO FINAL ---")

for aluno, nota in boletim.items():
    if nota >= 6.0:
        status = "Aprovado"
    else:
        status = "Reprovado"
        
    print(f"Aluno(a): {aluno} | Nota: {nota:.1f} | Status: {status}")
