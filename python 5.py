#crie uma função que recebe o nome de um produto, a quantidade que tem no estoque e o valor unitario do produto.
#retorne o valor total do meu estoque

def estoque(nome, quantidade, valorunitario):
    return quantidade*valorunitario
total = estoque("arroz", 30, 5)
print(total)

#de maneira diferente
#print(estoque("feijao", 20, 8.50))



