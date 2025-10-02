def quadrado ():
    lado = int(input('digiite o valor do lado '))
    area = lado * lado
    return area
    

def retangulo ():
    base = int(input('digite o valor da base '))
    altura = int(input('digite o valor da altura '))
    area = base * altura
    return area


def triangulo ():
    base = int(input('digite o valor da base '))
    altura = int(input('digite o valor da altura '))
    area = base * altura / 2
    return area
    

def circulo ():
    raio = int(input('digiite o valor do raio '))
    area = 3.14 * raio ** 2
    return area
    


def trapezio ():
    base = int(input('digite o valor da base '))
    Base = int(input('digite o valor da Base '))
    altura = int(input('digite o valor da altura '))
    area = (Base  +  base) * altura / 2
    return  area



def menu ():
    escolha =  input("Qual área deseja calcular ")
    
    
    if escolha == 'quadrado' :
        area = quadrado()
    elif escolha ==  'retangulo' :
        area =  retangulo()
    elif escolha ==  'triangulo' :
        area =  triangulo()
    elif escolha ==  'circulo' :
        area =  circulo()
    elif escolha ==  'trapezio' :
        area =  trapezio()
        
    print(area)
    
    continuar = input ('Deseja calcular novamente? ')
    if continuar == 'sim':
        menu()
        
        
menu()
