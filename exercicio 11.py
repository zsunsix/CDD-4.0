op = "5"
while op == "5":
    n1 = float(input("digite o primeiro numero"))
    n2 = float(input("digite o segundo numero"))
    op = input("selecione a operação")
    if op == "1":
        resultado = n1 + n2
        print(resultado)

    if op == "2":
        resultado = n1 - n2
        print(resultado)

    if op == "3":
        resultado = n1 * n2
        print(resultado)

    if op == "4":
        resultado = n1 / n2
        print(resultado)

    if op == "5":
        n1 = float(input("digite um novo numero"))
        n2 = float(input("digite um novo numero"))
        op = input("selecione a operação")

    if op == "6":
        print("sair")
