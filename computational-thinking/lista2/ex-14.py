valor_a_vista = float(input("Valor à vista: R$"))
valor_parcela = float(input("Valor de cada parcela: R$"))

valor_parcelado = valor_parcela * 10
percentual_desconto = ((valor_parcelado - valor_a_vista) / valor_a_vista) * 100

print(f"O percentual de desconto para pagamentos à vista é: {percentual_desconto}%")

