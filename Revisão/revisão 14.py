inicio = int(input("digite o horario do inicio da partida"))
fim = int(input("digite o horario do final da partida"))
total = fim - inicio

if total >= 24:
    print("o tempo execedeu o limite")

elif fim == inicio:
    print("durou 24 horas")

else:
    print(total)

