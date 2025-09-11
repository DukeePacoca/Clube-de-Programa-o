import random

opcoes = ["pedra", "papel", "tesoura"]


comp = random.randint(0 ,2)

escolha = input('Jokenpô: ')

if escolha == 'papel' and opcoes[comp] == 'pedra':
    print('Você Ganhou')
elif (escolha == 'pedra' and opcoes[comp] == 'tesoura'):
    print ('Você ganhou!')
elif (escolha == 'tesoura' and opcoes[comp] == 'papel'):
    print('Você Ganhou')
elif escolha == opcoes [comp]:
    print('Empate!')
else:
    print('Você perdeu!')
