print(" Morango R$2,50 o kg até 5kg\n Morango R$2,20 acima de 5kg\n Maçã R$ 1,80 o kg até 5kg\n Maçã R$ 1,50 o kg acima de 5kg")
morango = float(input("Digite a quantia de morangos desejados em kg: "))
maca = float(input("Digite a quantia de maçãs desejados em kg: "))
if morango >= 5:
    valormorango = morango * 2.20
else:
    valormorango = morango * 2.5
if maca >= 5:
    valormaca = maca * 1.5
else:
    valormaca = maca * 1.8
if morango + maca >= 8:
    print("Você ganhou mais 10% de desconto, o valor final da compra ficou em: ", (valormorango + valormaca) * 0.9)
else:
    print("O valor final da sua compra ficou em: ", valormorango + valormaca)