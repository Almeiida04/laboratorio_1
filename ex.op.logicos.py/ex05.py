print("Interrogatório sobre o assassinato de Michael Jackson. Responda (SIM/NÃO) ")

qtdSim = 0 
resposta = input("Telefonou para a vitima? (SIM ou NÃO) ").upper()

if resposta == "SIM":
    qtdSim = qtdSim + 1

resposta2 =  input("Esteve no local do crime? (SIM ou NÃO) ").upper()
if resposta2 == "SIM":
    qtdSim =  qtdSim + 1 

resposta3 = input("Mora perto da vítima? (SIM ou NÃO) ").upper()
if resposta3 == "SIM":
    qtdSim = qtdSim + 1

resposta4 = input("Devia para a vítima? (SIM ou NÃO) ").upper()
if resposta4 == "SIM":
    qtdSim = qtdSim + 1

resposta5 = input("Já trabalhou coma vítima? (SIM ou NÃO) ").upper()
if resposta5 == "SIM":
    qtdSim = qtdSim + 1

if qtdSim == 2:
    print("SUSPEITO DO CRIME! ")
elif qtdSim == 3 or qtdSim == 4:
    print("Cumplice do crime! ")
elif qtdSim == 5:
    print("Você é o assasino! ")
else:
    print("Você está liberado! ")