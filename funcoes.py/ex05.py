
def menu():
    print("1 - Sacar dinheiro")
    print("2 - Depositar dinheiro")
    print("3 - Mostar saldo")
    print("4 - Sair")
    opcao = int(input("Escolha: "))
    return opcao

def sacar(saldo):
    sacando = float(input("Quantidade sacar: "))
    if sacando <= saldo:
        saldo = saldo - sacando
        ver_saldo(saldo)
    else:
        print("Saldo ínvalido para saque!")
    return saldo

def depositar(saldo): 
    depositando = float(input("Quantidade depositar: "))
    saldo = saldo + depositando
    ver_saldo(saldo)
    return saldo

def ver_saldo(saldo):
    print(saldo)

def main():
    opcao = 0
    saldo = 0

    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            saldo = sacar(saldo)
        elif opcao == 2:
            saldo = depositar(saldo)
        elif opcao == 3:
            ver_saldo(saldo)
        elif opcao == 4:
            break
        else:
            print("erro")

main()