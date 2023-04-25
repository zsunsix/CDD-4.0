lista_numero = []
soma = []

for y in range (10):
    lista_numero.append(int(input("digite os numeros")))

num = int(input("digite o numero que deseja achar"))
for x in range (10):
    if num == lista_numero[x]:
         cc=cc+1


print(f"o numero", {num}, "existe", (cc), "vezes")
