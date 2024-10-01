while True:
    TotalCompra = 0
    NumeroProduto = 1
    while True:
        preco_produto = float(input("(Para confirmar a compra digite '0') Produto {}: R$: ".format(NumeroProduto)))
        if preco_produto == 0:
            break
        TotalCompra += preco_produto
        NumeroProduto += 1
    print("Total: R$ {}".format(TotalCompra))
    DinheiroCliente = float(input("Dinheiro: R$ "))
    troco = DinheiroCliente - TotalCompra
    print("Troco: R$ {}".format(troco))
    novaCompra = input("Deseja registrar uma nova compra? (sim/não): ").lower()
    if novaCompra != 'sim':
        break