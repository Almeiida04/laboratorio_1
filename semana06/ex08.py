elevador_a = 0
elevador_b = 0
elevador_c = 0
morador = 1

while morador <= 10:
    elevador = input(f"Morador {morador}, qual elevador você usa mais? (A, B ou C): ").upper()

    if elevador == 'A':
        elevador_a += 1
    elif elevador == 'B':
        elevador_b += 1
    else:
        elevador_c += 1

    morador += 1

total_votos = elevador_a + elevador_b + elevador_c
percentual_a = (elevador_a / total_votos) * 100
percentual_b = (elevador_b / total_votos) * 100
percentual_c = (elevador_c / total_votos) * 100

print("\nResultados:")
print(f"Elevador A: {elevador_a} votos ({percentual_a:.2f}%)")
print(f"Elevador B: {elevador_b} votos ({percentual_b:.2f}%)")
print(f"Elevador C: {elevador_c} votos ({percentual_c:.2f}%)")