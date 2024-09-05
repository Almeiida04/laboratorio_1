nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Sua média é {media}: ")

if media >= 9.0:
    print("Seu conceito é (A): ")
elif media >= 7.5:
    print("Seu conceito é (B): ")
elif media >= 6.0:
    print("Seu conceito é (C): ")
elif media >= 4.0:
    print("Seu conceito é (D): ")
else:
    print("Seu conceito é (E): ")
    