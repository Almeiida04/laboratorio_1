print("### DIGITE A CATEGORIA DA SUA CNH: ###")
print(" (A), (B), (C), (D), (E) ")
cnh = input("Digite a categoria da sua CNH: ").upper()

if cnh == 'A':
    print("Pode dirigir moto")
elif cnh == 'B':
    print("Pode dirigir carro")
elif cnh == 'C':
    print("Pode dirigir caminhão")
elif cnh == 'D':
    print("Pode dirigir ônibus")
elif cnh == 'E':
    print("Pode dirigir carreta")