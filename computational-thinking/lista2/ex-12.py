rm = int(input("Informe o seu RM: "))
soma = 0

while rm != 0:
    resto = rm % 10     
    rm = rm // 10
    soma += resto


print(f"A soma dos números do seu RM é {soma}")

