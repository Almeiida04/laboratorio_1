idades = []
pesos = []
cont = 0

while cont < 7:
    idade = int(input(f"Digite a idade da {cont+1}ª pessoa: "))
    peso = float(input(f"Digite o peso da {cont+1}ª pessoa: "))
    idades.append(idade)
    pesos.append(peso)
    cont += 1
    
media_idades = sum(idades) / len(idades)
print(f"A média das idades das 7 pessoas é: {media_idades:.2f} anos")