#faça uma função que conte quantas vogais tem num texto o rato roeu a roupa do rei de roma

def conta_vogais(string):
    string = string.lower()
    result = 0
    vogais = 'aeiou'
    for i in vogais:
        result += string.count(i)
    return result

print(conta_vogais('olaaa'))


#def contarvogais(t):
     #cont=0
     #for x in t:
          #if x in "aeiouAEIOU":
                #cont=+=1
    #print(cont)

#texto = "o rato roeu a roupa do rei de roma"
#contarvogais(texto)


