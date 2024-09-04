n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a sua opção: ")

if opcao == '1':
    somaNumeros = n1 + n2
    print(somaNumeros)
elif opcao == '2':
    subtracao = n1 - n2
    print(subtracao)
elif opcao == '3':
    multiplicacao = n1 * n2
    print(multiplicacao)
elif opcao == '4':
    divisao = n1 / n2
    print(divisao)