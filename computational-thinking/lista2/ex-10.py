metros = float(input("Quantidade percorrida (em metros): "))
segundos = float(input(f"Tempo que ele percorreu os {metros} metros (em segundos): "))

velocidade_media_si = metros / segundos
velocidade_media = velocidade_media_si * 3.6

print(f"Velocidade em m/s: {velocidade_media_si} \nVelocidade em km/h: {velocidade_media}")

