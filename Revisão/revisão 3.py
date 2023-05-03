idade = int(input("digite a idade"))
ano = 2023-idade
print("você nasceu em", ano)

pergunta = input("deseja colocar outra idade?")
while pergunta == "sim":
    idade = int(input("digite a idade"))
    ano = 2023 - idade
    print("você nasceu em", ano)


