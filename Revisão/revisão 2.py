num = int(input("digite um numero"))
while num != 0:
    if num >=0:
        print("positivo")

    else:
        print("negativo")
    break 
pergunta = input("deseja colocar outro numero?")
if pergunta == "sim":
    num = int(input("digite um numero"))
    if num != 0:
        if num >= 0:
            print("positivo")

        else:
            print("negativo")

