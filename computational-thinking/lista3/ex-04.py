time_a = input("Primeiro time: ")
time_b = input("Segundo time: ")

qtd_gols_a = int(input(f"Quantidade de gols do time {time_a}: "))
qtd_gols_b = int(input(f"Quantidade de gols do time {time_b}: "))

resultado = "Os times empataram"

if qtd_gols_a > qtd_gols_b:
    resultado = f"Vencedor: {time_a}"
elif qtd_gols_b > qtd_gols_a:
    resultado = f"Vencedor: {time_b}"

print(resultado)

