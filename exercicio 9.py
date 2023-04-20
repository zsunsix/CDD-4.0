nota1 = float(input("digite sua primeira nota"))
while nota1 <0 or nota1>10:
    print("digite sua nota valida")
    nota1 = float(input("digite sua primeira nota"))

nota2 = float(input("digite sua segunda nota"))
while nota2 <0 or nota2 >10:
     print("digite sua nota valida")
     nota2 = float(input("digite sua segunda nota"))
media = (nota1 + nota2)/2

print(media)

pergunta = input("deseja continuar")

while pergunta == "sim":
    nota1 = float(input("digite sua primeira nota"))
    while nota1 < 0 or nota1 > 10:
        print("digite sua nota valida")
        nota1 = float(input("digite sua primeira nota"))

    nota2 = float(input("digite sua segunda nota"))
    while nota2 < 0 or nota2 > 10:
        print("digite sua nota valida")
        nota2 = float(input("digite sua segunda nota"))
    media = (nota1 + nota2)/2

