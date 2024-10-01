idade = int(input("Digite a sua idade: "))
salario = float(input("Digite o seu salário: "))
sexo = input("Digite o seu sexo: F/M: ").upper()
estado_civil = str(input("Digite o seu estado civil 'S', 'C', 'V', 'D': ")).upper()

while idade < 0 or idade > 150 or salario < 0 or sexo != 'F' and sexo != 'M' or estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    if idade < 0 or idade > 150:
        idade = int(input("Digite novamente a sua idade: "))
    if salario < 0:
        salario = float(input("Digite novamente seu salário: "))
    if sexo != 'F' and sexo != 'M':
        sexo = input("Digite novamente seu sexo: ").upper()
    if estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
        estado_civil = input("Digite novamente seu estado civil: ").upper()
print("Dados inseridos corretamente! ")