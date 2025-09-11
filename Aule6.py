import random

opcoes = ["cara" , 'coroa']


moedas = random.randint(0 , 1)

escolha = input("Escolha cara ou coroa: ")

if escolha == opcoes[moedas]:
    print('Você ganhou!')
else:
    print('Você perdeu!')
