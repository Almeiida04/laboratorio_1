def numeros_inteiros():
    numeros = []
    for i in range(8):
        num = int(input("Digite um numero: "))
        numeros.append(num)
    return numeros       

def maior(numeros):
    maior_numero = numeros[0]  
    for num in numeros:
        if num > maior_numero:
            maior_numero = num 
    return maior_numero

def maiores30(numeros):
    contador = 0
    soma_maiores = 0
    for num in numeros:
        if num > 30:
            contador += 1
            soma_maiores += num
    return contador, soma_maiores

def soma(numeros):
    soma_num = 0
    for i in numeros:
        soma_num += i
    return soma_num 

def main():
    numeros_int = numeros_inteiros()
    print(f"Valores do vetor: {numeros_int}")
    maior_num = maior(numeros_int)
    print(f"O maior número do vetor é: {maior_num}")
    contador, soma_maiores_que_30 = maiores30(numeros_int)
    print(f"Quantidade de números maiores que 30: {contador}")
    print(f"Soma dos números maiores que 30: {soma_maiores_que_30}")
    soma_total = soma(numeros_int)
    print(f"Soma de todos os números do vetor: {soma_total}")

main()