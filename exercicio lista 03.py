notas_alunos= []
soma = 0
for x in range(5):
    notas_alunos.append(float(input("digite as notas dos alunos")))
for y in notas_alunos:
    soma+= y
media=soma/5
for nota in notas_alunos:
    if nota >= media:
        print(nota, "acima da media")
    else:
        print(nota, "abaixo da media")


#outro exercicio da forma do professor

alunos=[]
soma = 0
contador = 0
for x in range (5):
    alunos.append(float(input("digite as notas dos alunos")))

for y in range (5):
    soma+=alunos[y]
media=soma/5

for t in range (5):
    if media >= alunos[t]:
        contador+=1

    print("a quantidade de alunos acima da media é", contador)





