preco_original = float(input("Preço do produto: R$ "))
desconto = (float(input("Percentual de desconto: "))) / 100

preco_com_desconto = preco_original * (1 - desconto)
preco_com_aumento = preco_original * (1 + desconto)

print(f"O preço do produto com desconto é: R$ {preco_com_desconto}")
print(f"Caso o desconto fosse na verdade um aumento, o preço seria R$ {preco_com_aumento}")

