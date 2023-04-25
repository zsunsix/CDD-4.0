vetor = []
num = 0
maiorValor = 0
soma = 0
#add numeros no array e soma
for x in range(5):
    num = int(input("leia os valores inteiros"))
    vetor.append(num)


print(vetor)

for x in range(5):
    if maiorValor < vetor[x]:
        maiorValor = vetor[x]

print(maiorValor)

menorValor = vetor[0]
print(menorValor)

for x in range(5):
    if menorValor <= vetor[x]:
        menorValor = vetor[x]

print(menorValor)

for x in range (5):
    media = num/5
print(media)

for x in range (5):
    if num[x] %2 == 0:
        print(num[x])



