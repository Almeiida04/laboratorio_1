maiores_de_18 = 0
contador = 0

while contador < 10:
    idade = int(input("Digite a idade: "))
    if idade >= 18:
        maiores_de_18 += 1
    contador += 1

print(f"Há {maiores_de_18} pessoas com 18 anos ou mais.")