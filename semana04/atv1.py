print("Bem a loja do Almeidinha: ")
print("1 - Pagar a vista: ")
print("2 - Pagar em 2x vezes: ")
print("3 - Pagar em 3x vezes: ")
opcao = int(input("Digite uma opção: "))

valorCompra = float(input("Digite o valor da compra: "))

if opcao == 1:
    valorFinal = valorCompra * 0.5
    print("Valor da comora com desconto é {}".format(valorFinal))
elif opcao == 2:
    valorFinal = valorCompra * 1.15
    print("Valor da compra com juros é de {}".format(valorFinal))
elif opcao == 3:
    valorFinal = valorCompra * 1.30
    print("Valor da comora com juros é de {}".format(valorFinal))
else:
    print("Opção inválida! ")
    