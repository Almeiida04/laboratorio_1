def valorTotalLaranjas(totalLaranjas):
  if totalLaranjas <= 12:
    valorUnitario = 0.4
  else:
    valorUnitario = 0.25
  valorTotal = totalLaranjas * valorUnitario
  return valorTotal
totalLaranjas = int(input("Quantas laranjas você comprou? "))
valorTotal = valorTotalLaranjas(totalLaranjas)
print(f"O valor total da compra é de R${valorTotal}:")
