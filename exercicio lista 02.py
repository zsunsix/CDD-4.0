alunos = int(input("digite a quantidade de alunos da sala: "))
lista_alunos = []
for x in range (alunos):
    lista_alunos.append(input("digite o nome dos alunos"))
contador= 0
for aluno in lista_alunos:
    print(contador,aluno)
    contador += 1

    


