cont_pessoas = 0
soma_idade = 0

while cont_pessoas <= 15:
    idade_pessoas = int(input("Digite a sua idade: "))
    cont_pessoas += 1
    soma_idade += idade_pessoas
media_idades = soma_idade / cont_pessoas
if media_idades <= 25:
    print("Turma jovem: ")
elif media_idades >= 26 and media_idades <= 60:
    print("Turma adulta: ")
else:
    print("Turma idosa: ")
