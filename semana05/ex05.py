idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Você é de menor. ")
elif idade > 18 and idade < 60:
    print("Você é de maior. ")
else: 
    print("Você é idoso(a). ")
