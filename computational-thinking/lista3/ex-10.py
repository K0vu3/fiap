import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = b** - 4 * a * c

if delta >= 0: 
    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)
else: 
    print("Não existem raízes reais")

    
print(f"x1 = {x1} /nx2 = {x2}")


