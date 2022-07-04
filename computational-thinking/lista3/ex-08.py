idade = int(input("Idade: "))
result = "Informe uma idade válida!"

if idade >= 5 and idade <= 7:
    result = "Categoria: Infantil"
elif idade >= 8 and idade <= 10:
    result = "Categoria: Juvenil"
elif idade >= 11 and idade <= 15:
    result = "Categoria: Adolescente"
elif idade >= 16 and idade <= 30:
    result = "Categoria: Adulto"
elif idade > 30:
    result = "Categoria: Senior"

print(result)

