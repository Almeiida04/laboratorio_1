hora_atual = int(input("Digite a hora atual (0-23): "))

if hora_atual < 0 or hora_atual > 23:
    print("Erro: a hora deve estar entre 0 e 23.")
else:
    if (hora_atual >= 18 or hora_atual < 6):
        print("Período noturno.")
    else:
        print("Período diurno.")