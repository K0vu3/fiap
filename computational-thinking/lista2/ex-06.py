from cmath import pi
import math

raio = float(input("Informe o raio da circunferência: "))
PI = math.radians(180)

AREA_CIRCUNFERENCIA = PI * raio**2
PERIMETRO_CIRCUNFERENCIA = 2 * PI * raio


print(f"Área da circunferência: {AREA_CIRCUNFERENCIA} \nPerímetro da Circunferência: {PERIMETRO_CIRCUNFERENCIA}")

