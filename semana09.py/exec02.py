soma= 0
media = 0

for i in range (1, 11):
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero
media = soma / 10

print(f"A média dos números digitados é: {media:.2f}")