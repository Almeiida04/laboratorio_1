populacao_A = 80000
populacao_B = 200000
taxa_cresc_A = 0.03
taxa_cresc_B = 0.015
cont_anos = 0

while populacao_A < populacao_B:
    populacao_A += populacao_A * taxa_cresc_A
    populacao_B += populacao_B * taxa_cresc_B
    cont_anos += 1
print(f"Serão necessários {cont_anos}, para o país A, ultrapassar ou se igualar ao país B: ")