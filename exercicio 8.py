pin = "sunsix"
tentativa1 = 1
acesso = input("digite a senha")
while pin !=pin:
    tentativas = tentativas + 1
    print("senha incorreta, digite novamente: ")
    senha = input()
    print(tentativas)
    if tentativas>2 and senha!=pin:
        print ("senha bloqueada")
        break
else:
        print("Acesso liberado")




