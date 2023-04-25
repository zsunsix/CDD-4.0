lista_usuario = []
lista_senha = []

for x in range(5):
    lista_usuario.append(input("Nome de usuário: "))
    lista_senha.append(input("Digite a senha: "))

novo_usuario = input("Nome de usuário: ")
nova_senha = input("digite nova senha: ")
confusuario = False

for y in range (5):
    if novo_usuario == lista_usuario[y]:
     if nova_senha == lista_senha[y]:
         confusuario = True
         break
if confusuario:
    print("usuario a senha é correta")

else:
    print("usuario a senha é incorreta, tente novamente")




