palavra = input("Digite uma palavra: ")

vogais_encontradas = []

vogais = "aeiouAEIOU"

for letra in palavra:
    
    if letra in vogais:
        vogais_encontradas.append(letra)

print("Vogais encontradas:", vogais_encontradas)
