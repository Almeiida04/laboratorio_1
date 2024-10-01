numero = int(input("Digite o numero que deseja calcular seu fatorail: "))
contador = numero
fatorial = 1

while contador > 0:
    print(contador)
    fatorial *= contador
    contador -= 1
print("O fatorial de {} é de: {} ".format(numero, fatorial))