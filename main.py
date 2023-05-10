def menu():
    print(f'''
    ######### MENU ##########
    
1 - SOMA
2 - SUBTRAÇÃO
3 - MULTIPLICAÇÃO
4 - DIVISÃO
5 - SAIR 

####### MENU #########
    ''')

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

while True:
    menu()
    opcao = int(input("qual sua escolha: "))

    if opcao == 5:
        break

    n1 = float(input("digite o primeiro numero: "))
    n2 = float(input("digite o segundo numero: "))

    if opcao == 1:

        print(soma(n1,n2))

    elif opcao == 2:

        print(subtracao(n1, n2))

    elif opcao == 3:
       print(multiplicacao(n1,n2))

    elif opcao == 4:
       print(divisao(n1,n2))



