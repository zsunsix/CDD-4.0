lista_medias=[]
nota1 = float(int(input("digite a primeira nota")))
nota2 = float(int(input("digite a segunda nota")))


media = (nota1+nota2)/2

lista_medias.append(media)
print(media)
pergunta = input("Deseja continuar?")
if pergunta == "sim":
    nota1 = float(int(input("digite uma nota")))
    nota2 = float(int(input("digite duas nota")))

media = (nota1 + nota2) / 2

if media >=7:
    print("o aluno está aprovado")

elif media >=4:
    print("o aluno está em recuperação")

else:
    print("o aluno está reprovado")

pergunta = input("Deseja continuar?")
print(lista_medias)




