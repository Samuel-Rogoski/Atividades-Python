numero = int(input("Digite um número de 1 a 10: "))

print(f"\nTabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
