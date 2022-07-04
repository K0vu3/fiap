num_a = int(input("Primeiro número: "))
num_b = int(input("Segundo número: "))
resposta = "Os números são iguais"

if num_a > num_b:
    resposta = f"O maior número é o {num_a}"
elif num_b > num_a:
    resposta = f"O maior número é o {num_b}"

print(resposta)

