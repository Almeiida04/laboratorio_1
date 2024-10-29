maiorIdd = 0
femininoVL = 0

olhosAzuis = 0
olhosVerdes = 0
olhosCastanhos = 0

cabLoiros = 0
cabCastanhos = 0
cabPretos = 0

sexoMasc = 0
sexoFem = 0

for i in range(15):
    idd = int(input("Insira a sua idade: "))
    if idd > maiorIdd:
        maiorIdd = idd

    while True:
        s = input("Sexo (M/F): ").upper()
        if s == 'M' or s == 'F':
            break
    if s == 'M':
        sexoMasc += 1
    else:
        sexoFem += 1

    while True:
        o = input("Cor dos olhos ('A' p/ Azul, 'V' p/ Verdes ou 'C' P/ Castanhos): ").upper()
        if o == 'A' or o == 'V' or o == 'C':
            break
    if o == 'A':
        olhosAzuis += 1
    elif o == 'V':
        olhosVerdes += 1
    else:
        olhosCastanhos += 1

    while True:
        c = input("Cor dos cabelos ('L' p/ Loiros, 'C' p/ Castanhos ou 'P' p/ Pretos): ").upper()
        if c == 'L' or c == 'C' or c == 'P':
            break
    if c == 'L':
        cabLoiros += 1
    elif c == 'C':
        cabCastanhos += 1
    else:
        cabPretos += 1

    if s == 'F' and idd >= 18 and idd <= 35 and o == 'V' and c == 'L':
        femininoVL += 1

print(f"A maior idade do grupo é {maiorIdd}: ")
print(f"A quantidade de indivíduos do sexo feminino, cuja idade está entre 18 e 35 anos e que tenham olhos verdes e cabelos loiros é {femininoVL}: ")
print(f"A porcentagem de pessoas com os olhos azuis é {olhosAzuis/15*100}%: ")
print(f"A porcentagem de pessoas com os olhos verdes é {olhosVerdes/15*100}%: ")
print(f"A porcentagem de pessoas com os olhos castanhos é {olhosCastanhos/15*100}%: ")
print(f"A porcentagem de pessoas com os cabelos loiros é {cabLoiros/15*100}%: ")
print(f"A porcentagem de pessoas com os cabelos castanhos é {cabCastanhos/15*100}%: ")
print(f"A porcentagem de pessoas com os cabelos pretos é {cabPretos/15*100}%: ")
print(f"A porcentagem de pessoas do sexo masculino é {sexoMasc/15*100}%: ")
print(f"A porcentagem de pessoas do sexo feminino é {sexoFem/15*100}%: ")