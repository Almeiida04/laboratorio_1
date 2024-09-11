nota = float(input("Digite uma nota: "))

if nota < 5:
    print("Você está reprovado(a). ")
elif nota >= 5 and nota < 7:
    print("Você está em recuperação. ")
else:
    print("Você foi aprovado! ")
