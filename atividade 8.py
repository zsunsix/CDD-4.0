vetorA = []
vetorB = []
vetorC = []

opc = int(input("digite um valor"))
for x in range (opc):
    vetorA.append(int(input("digite um número novo")))
    vetorB.append(int(input("digite um número novo")))

for y in range (opc):
    vetorC.append(vetorA[y] + vetorB[y])
    print()

print(vetorA)
print(vetorB)
print(vetorC)



