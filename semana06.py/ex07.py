base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

while expoente > 0:
    resultado *= base
    expoente -= 1
print(f"O resultado de {base}, elevador ao {expoente}, é {resultado}: ")