numero = int(input("Digite um número:"))

if numero <= 1:
    print("O número {} não é primo.".format(numero))
elif numero == 2:
    print("O número {} é primo.".format(numero))
else:
    divisor = 2
    while divisor <= numero // 2:
        if numero % divisor == 0:
            print("O número {} não é primo.".format(numero))
            break
        divisor +=1
    else:
        print("O número {} é primo.".format(numero))