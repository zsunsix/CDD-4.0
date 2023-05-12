def texto_quant(texto):
    texto_2= '' .join(texto.split())
    return len(texto_2), texto [:: -1]
print(texto_quant("Agora me ve e agora não me vê mais"))


#da minha forma de logica
#nova_string = ""
#frase = input('Digite uma frase: ')
#print(' Você digitou: {}'.format(frase))
#for palavra in frase.split(" "):
    #nova_string += palavra[::-1]+" "
#print('A frase que você digitou invertida fica: {}'.format(nova_string))

#da forma do professor
#def letras(t):
     #cont=0
     #textoi=""
     #for x in t:
          #if x not in " ":
                #cont+=1
    #print(cont)
    #for y in range(len(t)-1,-1,-1):
         #textoi+=t[t]
    #print(textoi)
