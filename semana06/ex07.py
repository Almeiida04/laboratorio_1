contador = 0
numeros_entre_30_e_90 = 0

while contador < 10:
    numero = int(input(f"Digite o {contador+1} número: "))
    if 30 <= numero <= 90:
        numeros_entre_30_e_90 += 1
    contador += 1
print(f"Há {numeros_entre_30_e_90} números entre 30 e 90. ")