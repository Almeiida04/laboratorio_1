number = 37
user_number = 0

while user_number != number:
    user_number = int(input("Digite um número: "))
    if user_number < number:
        print("Tente um número maior: ")
    elif user_number > number:
        print("Tente um número menor: ")
    else:
        print("Você acertou! ")