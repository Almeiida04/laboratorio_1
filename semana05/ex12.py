numero_dia = int(input("Digite um número de 1 a 7 (1 para Domingo): "))
dias_da_semana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]

if 1 <= numero_dia <= 7:
    print(dias_da_semana[numero_dia - 1])
else:
    print("Número inválido. Digite um número entre 1 e 7.")