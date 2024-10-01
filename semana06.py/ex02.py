number = int(input("Digite um numero para sabermos a soma de 1 até ele:  "))
count = 0
soma = 0
while count != number + 1:
    soma += count
    count +=1

print(f"O valor da soma de 1 até {number} é: {soma}")