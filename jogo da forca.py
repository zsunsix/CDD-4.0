import random  #importa uma biblioteca que trás funções aleatorias

palavras = ["harry potter", "herminone", "draco", "weasley", "snape"]

palavra = random.choice(palavras)
tentativas = 0
chances = 5


letra_escolhida = [] #uma lista criada para as letras que já foram escolhidas
palavra_atual = ["_"]*len(palavra) #ficará no lugar das palavras que não foram escolhidas
#len vai colocar "_" a quantia equivalente a palavra

print("Seja bem vindo ao leve jogo de Hogwarts")
print("Você terá 5 chances")
print("Boa sorte, caro bruxo")

while tentativas < chances and ' '.join(palavra_atual) != palavra:

    letra = input("\nQual letra você deseja tentar, bruxo?\n ")

    #caso venha acontecer de escolher uma letra repetida

    while letra in letra_escolhida:
        print("Você já escolheu essa palavra, tente outra!")
        letra = input("\nQual letra você deseja tentar, bruxo?\n")

        letra_escolhida.append(letra)

        if letra in palavra:
            print("Você acertou a letra, ponto para griffinoria!\n")
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    palavra_atual[i] = letra
        else:
            print("Você errou bruxo, que lamentável")
            tentativas = tentativas + 1

        #quantas tentativas o bruxo vai ter

        print(f'Você já fez {tentativas} tentativas erradas e você ainda tem {chances - tentativas} tentativas.')

        #estado atual da palavra

        print("Esse é o estado atual")
        print(palavra_atual)

        #quais as letras que o bruxo já tentou

        print("As letras que você já tentou bruxo, são: ")
        for item in letra_escolhida:
            print(item, end=" ")

    if tentativas == chances:
        print("Você perdeu bruxo, merece o feitiço avada kedrava\n")

    else:
        print("Parabéns bruxo, você ganhou, merece um banquete\n")

    print(f' A palavra era, {palavra}')






