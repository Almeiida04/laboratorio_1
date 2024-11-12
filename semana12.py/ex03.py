def ler_valores():
    valores = []  
    for i in range(10): 
        valor = int(input(f"Digite o valor {i+1}: "))
        while valor in valores:  
            print("Valor repetido! Digite outro valor.")  
            valor = int(input(f"Digite o valor {i+1}: "))
        valores.append(valor)  
    return valores  

def exibir_pares_e_posicoes(numeros):
    for i in range(len(numeros)):  
        num = numeros[i] 
        if num % 2 == 0:  
            print(f"O número {num} é par e está na posição {i}") 

def main():
    numeros = ler_valores() 
    exibir_pares_e_posicoes(numeros)  

main()