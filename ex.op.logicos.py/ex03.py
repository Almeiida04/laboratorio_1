nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"Sua média é {media}: ")

frequencia = int(input("Digite a sua frequência: "))

if media >= 7 and frequencia >= 75:
    print("Aprovado! ")
elif media <= 7 and frequencia >= 75:
    print("Você está em exame. ")
else:
    print("Reprovado! ")