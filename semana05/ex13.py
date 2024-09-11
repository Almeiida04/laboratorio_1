dia_juliano = int(input("Digite o dia juliano (1-366): "))

if dia_juliano < 1 or dia_juliano > 366:
    print("Erro: dia juliano deve estar entre 1 e 366.")
else:
    if dia_juliano <= 31:
        mes = "janeiro"
        dia_do_mes = dia_juliano
    elif dia_juliano <= 31 + 29:
        mes = "fevereiro"
        dia_do_mes = dia_juliano - 31
    elif dia_juliano <= 31 + 29 + 31:
        mes = "março"
        dia_do_mes = dia_juliano - (31 + 29)
    elif dia_juliano <= 31 + 29 + 31 + 30:
        mes = "abril"
        dia_do_mes = dia_juliano - (31 + 29 + 31)
    elif dia_juliano <= 31 + 29 + 31 + 30 + 31:
        mes = "maio"
        dia_do_mes = dia_juliano - (31 + 29 + 31 + 30)
    elif dia_juliano <= 31 + 29 + 31 + 30 + 31 + 30:
        mes = "junho"
        dia_do_mes = dia_juliano - (31 + 29 + 31 + 30 + 31)
    elif dia_juliano <= 31 + 29 + 31 + 30 + 31 + 30 + 31:
        mes = "julho"
        dia_do_mes = dia_juliano - (31 + 29 + 31 + 30 + 31 + 30)
    elif dia_juliano <= 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31:
        mes = "agosto"
        dia_do_mes = dia_juliano - (31 + 29 + 31 + 30 + 31 + 30 + 31)
    elif dia_juliano <= 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30:
        mes = "setembro"
        dia_do_mes = dia_juliano - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31)
    elif dia_juliano <= 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31:
        mes = "outubro"
        dia_do_mes = dia_juliano - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30)
    elif dia_juliano <= 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30:
        mes = "novembro"
        dia_do_mes = dia_juliano - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31)
    else:
        mes = "dezembro"
        dia_do_mes = dia_juliano - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30)
    print(f"{dia_do_mes} de {mes} de 2024")