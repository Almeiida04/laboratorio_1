cont_10 = 0

while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    if num == 10:
        cont_10 += 1
print("O número 10 foi digitado", cont_10, "vezes.")