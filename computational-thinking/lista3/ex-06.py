num_a = int(input("A: "))
num_b = int(input("B: "))

result = f"{num_a} não é divisível por {num_b}"

if num_a % num_b == 0:
    result = f"{num_a} é divisível por {num_b}"

print(result)

