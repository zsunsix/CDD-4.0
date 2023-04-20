'''Questão 3 - salario'''
nome = input("Digite seu nome")
idade = int(input("Digite sua idade"))
salario = float(input("Digite seu salario"))
percentualAumento = float(input("Digite seu aumento"))
aumento = (percentualAumento/100)*salario

novoSalario = salario + aumento

print(nome,idade,salario, novoSalario)
