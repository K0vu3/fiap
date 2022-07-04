qtd_camisas = int(input("Quantidade de camisas: "))
qtd_calcas = int(input("Quantidade de calças: "))
qtd_sapatos = int(input("Quantidade de pares de sapatos: "))

qtd_vestimentas = qtd_sapatos * qtd_camisas * qtd_calcas

print(f"A quantidade total de formas diferentes de se vestir é: {qtd_vestimentas}")

