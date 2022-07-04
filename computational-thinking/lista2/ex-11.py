salario_sem_aumento = float(input("Salário antes do aumento: R$ "))
salario_com_aumento = float(input("Salário após do aumento: R$ "))

percentual_aumento = ((salario_com_aumento - salario_sem_aumento) / salario_sem_aumento) * 100

print(f"O percentual de aumento foi de {percentual_aumento}%")

