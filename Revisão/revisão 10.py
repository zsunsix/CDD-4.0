validos = []
brancos = []
nulos = []

eleitores = int(input("digite a quantidade de eleitores"))

for valido in range (1):
    validos.append(int(input("Quantos votos validos?")))
print()

for branco in range (1):
    brancos.append(int(input("Quantos votos em brancos?")))
print()

for nulo in range (1):
    nulos.append(int(input("Quantos votos nulos?")))
print()

total = validos[valido] + brancos[branco] + nulos[nulo]
perValido = (validos[valido]/total)* 100
perBranco = (brancos[branco]/total)* 100
perNulo = (nulos[nulo]/total)* 100

if total > eleitores:
    print("Algo de certo não está errado")
else:
    print(f'{total} e os percentuais são: {perValido}% pros validos; {perBranco}% pros brancos e {perNulo}% pros nulos')





