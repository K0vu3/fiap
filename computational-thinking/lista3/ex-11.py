preco_produto = float(input("Preço do produto: "))
print("1 - A vista em dinheiro ou cheque, recebe 10% de desconto\n2 - A vista no cartão de crédito, recebe 5% de desconto\n3 - sEm duas vezes, preço normal de etiqueta sem juros\n4 - Em quatro vezes, preço normal de etiqueta mais juros de 7%")
codigo_pagamento = int(input("Código de pagamento: "))

if codigo_pagamento == 1:
    preco_calculado = preco_produto * 0.9
elif codigo_pagamento == 2:
    preco_calculado = preco_produto * 0.95
elif codigo_pagamento == 3:
    preco_calculado = preco_produto
elif codigo_pagamento == 4:
    preco_calculado = preco_produto * 1.07

print(f"Preço calculado: R$ {preco_calculado}")

