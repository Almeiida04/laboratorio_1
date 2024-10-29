opiniao_A = 0
opiniao_B = 0
opiniao_C = 0

for i in range(20):
    opiniao = input("Qual jornal você lê mais em Santa Maria (A, B ou C)? ").upper()
    if opiniao == "A":
        opiniao_A += 1
    elif opiniao == "B":
        opiniao_B += 1
    elif opiniao == "C":
        opiniao_C += 1
    else:
        print("Opinião inválida. Por favor, insira A, B ou C.")

total_pessoas = 20
porcent_A = (opiniao_A / total_pessoas) * 100
porcent_B = (opiniao_B / total_pessoas) * 100
porcent_C = (opiniao_C / total_pessoas) * 100

porcentagens = [('A', porcent_A), ('B', porcent_B), ('C', porcent_C)]

porcentagens.sort(key=lambda x: x[1])

print("Porcentagem de leitores de cada jornal em ordem crescente:")
for jornal, porcentagem in porcentagens:
    print(f"Jornal {jornal}: {porcentagem:.2f}%")
