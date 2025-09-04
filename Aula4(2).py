import random 
#import os



#os.system('cls')

while 1:
    num = random.randint(1, 100)
    tentativa = 0

    while 1:
        tentativa += 1
        print(f'Tentativa {tentativa}')
        palpite = input('Digite um número: ')
        palpite = int(palpite)
        
        
        if (palpite <= 0 or palpite > 100) :
            print ('Número inválido')
        elif palpite == num:
            print ('Você venceu')
            break
        elif palpite <  num :
            print ("O número é maior")
            
        elif palpite >  num :
            print ("O número é menor")

        
        
    continuar = input("Continuar? (s/n)")
    if continuar == "n" :
        break
