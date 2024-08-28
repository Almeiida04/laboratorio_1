valorHora = 35
horasTrabalhadas = int(input("Digite quantas horas trabalhou no mês: "))
salarioFinal = horasTrabalhadas * valorHora

if salarioFinal <= 1000:
    salarioFinal = salarioFinal + 300
    print("Você recebeu um aumento de 300 reais, seu salário agora é de: ", salarioFinal)

else:
    print("Seu salário final é de: ", salarioFinal)


