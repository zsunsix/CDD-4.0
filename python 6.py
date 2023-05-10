#faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere 'P', se seu
# argumento for positivo, e 'N', se seu argumento for negativo e Z se o argumento for zero


def pn(n):
    if n > 0:
        return ('P')
    elif n == 0:
        return ('N')
    elif n < 0:
        return ('Z')

num = int(input('digite um número: '))
resultado = pn(num)
print('Este número é',  resultado, end=' ')








