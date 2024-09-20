
saldoAtual = int(input("Digite seu saldo atual: "))
opcao = 0 

while opcao != 4:
    print("1 - Sacar\n2 - Depositar\n3 - Saldo\n4 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao ==  1:
        saque = float(input("Quanto deseja sacar: "))
        if saque > saldoAtual:
            print("Saldo insuficiente. ")
        else:
            saldoAtual = saldoAtual - saque
            print ("Saque efetuado com sucesse seu saldo agora é de: ", saldoAtual)
    elif opcao == 2:
        deposito = float(input("Quanto deseja depositar: "))
        saldoAtual =  saldoAtual + deposito
        print("Deposito efetuado com sucesse, seu saldo agora é de: ", saldoAtual)
    elif opcao == 3:
        print("Seu saldo atual é de: ", saldoAtual)
    elif opcao == 4:
        print("Até breve! ")
    else:
        print("Opção invalida! ")
    
       