valorCompra = float(input("Digite o valor da compra em R$: "))
categoriaCliente = input("Digite a categoria do cliente (Regular, VIP ou Platinum): ").lower()

if categoriaCliente == "regular":
    if valorCompra > 100:
        desconto = 0.05
    else:
        desconto = 0.0
elif categoriaCliente == "vip":
    if valorCompra > 500:
        desconto = 0.20
    elif valorCompra > 100:
        desconto = 0.10 
    else:
        desconto = 0.0
elif categoriaCliente == "platinum":
    if valorCompra > 500:
        desconto = 0.25  
    elif valorCompra > 100:
        desconto = 0.15  
    else:
        desconto = 0.0
else:
    print("Erro: Categoria inválida.")
    desconto = 0.0

valorDesconto = valorCompra * desconto
valorFinal = valorCompra - valorDesconto

if desconto > 0:
    print(f"Você recebeu {desconto * 100}% de desconto. Valor final: R${valorFinal:.2f}.")
else:
    print(f"Valor final: R${valorFinal:.2f}.")