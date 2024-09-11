idade = int(input("Digite a sua idade: "))
genero = input("Digite o seu sexo: (Masculino ou Feminino): ").lower()

if idade < 18:
    print("Adolescente. ")
elif genero == "masculino" and idade > 18:
    print("Homem adulto. ")
elif genero == "feminino" and idade > 18:
    print("Mulher adulta. ")