def somaImposto(taxaImposto, custo):
  taxa_decimal = taxaImposto / 100
  imposto = custo * taxa_decimal
  custo += imposto
  return custo

custo_original = 100
taxa = 10  
novo_custo = somaImposto(taxa, custo_original)

print("O novo custo com imposto é:", novo_custo)