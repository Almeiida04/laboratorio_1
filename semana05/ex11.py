temperatura = float(input("Digite quantos graus celsius faz agora na sua cidade: "))

if temperatura < 10:
    print("A temperatura é fria. ")
elif temperatura == 10 or temperatura <= 25:
    print("A temperatura está agradável. ")
elif temperatura > 25:
    print("A temperatura esá quente. ")
