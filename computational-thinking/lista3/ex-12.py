media_semestre_1 = float(input("Média do primeiro semestre: "))
media_semestre_2 = float(input("Média do segundo semestre: "))
total_aulas = int(input("Total de aulas: "))
aulas_assistidas = int(input("Aulas assistidas: "))

frequencia = aulas_assistidas >= (0.70 * total_aulas)
media_final = ((media_semestre_1 * 4) + (media_semestre_2 * 6)) / 10
aprovado = media_final >= 6

result = f"Média: {media_final} \nVocê está de exame"

if frequencia and aprovado:
    result = f"Média: {media_final} \nVocê está Aprovado"


print(result)

