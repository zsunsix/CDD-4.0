#faça um codigo para ler 5 nomes de usuarios e suas respectivas senhas, e armazenar cada lista em um array
#diferente, apos completar a digitação, imprimir, nome, senha e posição dos dados no array

lista_usuario = []
lista_senha = []
for x in range (5):
 lista_usuario.append(input("digite o nome: "))
 lista_senha.append(input("digite a senha: "))

print(lista_usuario)
print(lista_senha)

for y in range (5):
    print(y, lista_usuario, lista_senha[y])

    





