def ler_valores():
    valores = []  
    for i in range(10):  
        valor = int(input(f"Digite o valor {i+1}: "))
        while valor in valores:  
            print("Valor repetido! Digite outro valor.")  
            valor = int(input(f"Digite o valor {i+1}: "))
        valores.append(valor)  
    return valores  

def criar_vetor_b(numeros):
    vetor_b = numeros[::-1]  
    print(f'Vetor A: {numeros}')  
    print(f'Vetor B (invertido): {vetor_b}')  
    
def main():
    numeros = ler_valores()  
    criar_vetor_b(numeros)  

main()