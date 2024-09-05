print("Digite as medidas dos três lados de um triângulo: ")

lado1 = float(input("Digite a primeira medida: "))
lado2 = float(input("Digite a segunda medida: "))
lado3 = float(input("Digite a terceira medida: "))

if lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
    print("Esse é um triângulo Equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("Esse triângulo é Ísosceles")
else:
    print("Seu triângulo é Escaleno")
