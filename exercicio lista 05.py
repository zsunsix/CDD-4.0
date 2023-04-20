#faça um codigo para ler 20 (5) numeros e armazenar em um vetor. apos a leitura total dos 20 (5) numeros
#o codigo deve escrever esses 20 numeros lidos na ordem reversa.

lista = []
for x in range(5):
    lista.append(int(input("digite um numero: ")))
for y in range(-1, -6, -1):
    print(lista[y])
#está percorrendo o indice no negativo ao contrario usando range negativo (1, 2, 3, 4 // -4, -3, -2, -1)






