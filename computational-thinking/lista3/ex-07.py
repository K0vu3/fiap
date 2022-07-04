import math

num = int(input("Informe um número: "))
result = f"{num} não possui raíz real"

if num > 0:
    raiz = math.sqrt(num)
    result = f"A raíz quadrada de {num} é {raiz}"

print(result)

