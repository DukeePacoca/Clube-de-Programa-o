def soma (val1, val2):
    resultado = val1 + val2
    print (resultado)
    
def subtracao (val1, val2):
    resultado2 = val1 - val2
    print (resultado2)

def multiplicacao (val1, val2):
    resultado3 = val1 * val2
    print (resultado3)
    
def divisao (val1, val2):
    resultado4 = val1 / val2
    print (resultado4)
    
def potencia (val1,val2):
    resultado5 = val1 ** val2
    print (resultado5)
    
def radiciacao (val1):
    resultado6 = val1 ** 0.5
    print (resultado6)
while 1:
    print ('Não divida por 0!')
    operacao = input ("Escolha a operação: ")
    num1 = input ("Esolha o número: ")
    num1 = int(num1)
    if operacao != "radiciacao" :
        num2 = input ("Escolha mais um número: ")
        num2 = int(num2)



    if operacao == 'soma' or operacao == '+' or operacao == 'ss' :
        soma (num1, num2)
    elif operacao == 'subtracao' or operacao == '-' or operacao == 's' :
        subtracao (num1, num2)
    elif operacao == 'multiplicacao' or operacao == '*' or operacao == 'm' :
        multiplicacao (num1, num2)
    elif operacao == 'divisao' or operacao == '/' or operacao == 'd':
        divisao(num1, num2)
    elif operacao == 'potencia' :
        potencia (num1, num2)
    elif operacao == 'radiciacao' :
        radiciacao (num1)
    continuar = input ('Deseja jogar novamente? ')
    if continuar == 'nao':
        break
