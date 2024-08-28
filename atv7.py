altura = float(input("Digite a sua altura: "))
sexo = (input(" Digite (M) para masculino e (F) para feminino: ")).upper

if sexo == "F":
    pesoIdeal = (62.1 * altura) -44.7
    print("Peso ideal para você mulher: ", pesoIdeal)
else:
    pesoIdeal = (72.7 * altura) - 58
    print ("Peso ideal para você homem: ", pesoIdeal)

