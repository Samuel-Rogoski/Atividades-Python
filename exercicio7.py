senha_secreta = "python123"

senha_usuario = ""

while senha_usuario != senha_secreta:
    senha_usuario = input("Digite a senha de acesso: ")
    
    if senha_usuario != senha_secreta:
        print("Senha incorreta! Tente novamente.")

print("Acesso Liberado")
