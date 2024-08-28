num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))

if num1 == num2:
    print("Os números não podem serem iguais!" )

else:
    menorNumero = min(num1, num2)
    maiorNumero = max(num1, num2)
    print("A ordem crescende dos números é: ", menorNumero, maiorNumero)