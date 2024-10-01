contadorIdade = 0
somaIdade = 0
maiorIdade = 0
menorIdade = 300

while contadorIdade < 25:
    idade = int(input("Digite sua idade:"))
    contadorIdade += 1
    somaIdade += idade 
    mediaIdade = somaIdade / contadorIdade
    if idade > maiorIdade:
        maiorIdade = idade
    elif idade < menorIdade:
        menorIdade = idade
print("Maior idade {}\nMenor idade {}\nMédia das idade{}".format(maiorIdade,menorIdade,mediaIdade))