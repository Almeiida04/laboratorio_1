nome = str(input("Digite o seu nome: "))
salario = float(input("Digite o seu salário: "))
tempoServico = float(input("Digite seu tempo de serviço: "))

if tempoServico <= 5 and salario <= 2000:
    salario = (salario * 0.10)
    print(f"Você recebeu um aumento de 10%, seu salário agora é de R${salario}: ")
elif tempoServico >= 5 and salario >= 2000:
    salario = (salario * 0.05)
    print(f"Você recebeu um aumento de 5%, seu salário agora é de R${salario}: ")