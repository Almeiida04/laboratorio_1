senha = str(input("Digite a sua senha: "))

if len(senha) > 8 and '@' in senha:
    print("Senha válida")
else:
    print("Senha inválida")