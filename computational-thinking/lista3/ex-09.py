num_a = int(input())
operacao = input()
num_b = int(input())

if operacao == "+":
    result = num_a + num_b
elif operacao == "-":
    result = num_a - num_b
elif operacao == "*":
    result = num_a * num_b
elif operacao == "/":
    if num_b == 0:
        result = "Não é possível realizar a divisão por 0"
    else:
        result = num_a / num_b
else:
    result = "Erro"

print(result)

