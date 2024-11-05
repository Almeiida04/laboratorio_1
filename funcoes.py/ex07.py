def converter_24_para_12(hora, minuto):
    hora_12 = hora % 12
    periodo = "AM" if hora < 12 else "PM"
    return f"{hora_12 or 12}:{minuto:02d} {periodo}"

hora = int(input("Digite a hora (0-23): "))
minuto = int(input("Digite os minutos (0-59): "))

resultado = converter_24_para_12(hora, minuto)
print(resultado)