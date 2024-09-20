opcao = 0
somaIdade = 0
qtdPessoas = 0
somaAltura = 0

while opcao != 3:
    print("1 - Cadastrar\n2 - Mostrar média parcial de altura e idade\n3 - Sair ")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        idade= int(input("Digite a sua idade: "))
        altura = float(input("Digite a sua altura: "))
        somaIdade = somaIdade + idade
        somaAltura = somaAltura + altura
        qtdPessoas = qtdPessoas + 1 
        print("### Cadastrado com sucesso! ###")
    elif opcao == 2:
        if qtdPessoas == 0:
            print("Nenhuma pessoa cadastrada!")
        else:
            mediaIdade = somaIdade / qtdPessoas
            mediaAltura = somaAltura / qtdPessoas
        print("A média parcial de idade é:{}\n, a média parcial de altura é {}: ".format(mediaIdade, mediaAltura))
    elif opcao == 3:
        if qtdPessoas == 0:
            print("Até breve, nenhuma pessoa cadastrada! ")
        else:
            mediaIdade = somaIdade / qtdPessoas
            mediaAltura = somaAltura / qtdPessoas
            print("A média de altura é {} a media de idade é {}: ".format(mediaAltura, mediaIdade))
    else: 
        print("Opção invalida! ")
