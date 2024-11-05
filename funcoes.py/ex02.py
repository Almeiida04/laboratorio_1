def dobro(num):
    return num * 2
def triplo(num):
    return num * 3

def main():
    num = int(input("Digite um valor: "))

    dobroValor = dobro(num)
    triploValor = triplo(num)
    print(f"O dobro de {num} é: {dobroValor}")
    print(f"O triplo de {num} é: {triploValor}")
main()
