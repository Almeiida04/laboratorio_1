idades = []
sexos = []
salarios = []
cont = 0

while cont < 4:
    idade = int(input(f"Digite a idade da {cont+1}ª pessoa: "))
    sexo = str(input(f"Digite o sexo (M/F) da {cont+1}ª pessoa: " )).upper()
    salario = float(input(f"Digite o salário da {cont+1}ª pessoa: "))
    idades.append(idade)
    sexos.append(sexo)
    salarios.append(salario)
    cont += 1
media_salarios = sum(salarios) / len(salarios)
print(f"A média dos salários das 10 pessoas é: {media_salarios:.2f} reais: ")

maior_idade = max(idades) 
menor_idade = min(idades)
print(f"A maior idade do grupo é {maior_idade}, e a menor idade é {menor_idade}: ")

mulheres_ate_10k = 0
i = 0
while i < len(sexos):
    if sexos[i] == 'F' and salarios[i] <= 10000:
        mulheres_ate_10k += 1
    i += 1
print(f"A quantidade de mulheres com salário até R$10000,00 é: {mulheres_ate_10k} ")