dias_uteis = int(input("Total de dias úteis do mês: "))
horas_trabalhadas = int(input("Total de horas trabalhadas no mês: "))
salario_por_hora = float(input("Sálario por hora trabalhada: "))

jornada_diaria = 8
hora_extra = horas_trabalhadas - (dias_uteis * jornada_diaria)
salario = salario_por_hora * horas_trabalhadas
salario_extra = hora_extra * (salario_por_hora * 0.5)
salario_total = salario + salario_extra

result = f"Salaário final: R${salario_total}"

if hora_extra > 0:
    result = f"Salario final (com hora extra): R${salario_total} \nHora Extra: R${salario_extra}"

print(result)

