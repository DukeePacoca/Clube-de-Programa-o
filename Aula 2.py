print('Hello World')

nota1 = input ('Digite a  primeira nota: ')
nota2 = input ('Digite a  segunda nota: ')
nota3 = input ('Digite a  terceira nota: ')
nota4 = input ('Digite a  quarta nota: ')

nota1 = int(nota1)
nota2 = int(nota2)
nota3 = int(nota3)
nota4 = int(nota4)

resultado = (nota1 + nota2 + nota3 + nota4)
resultado2 = (resultado / 4)

print(resultado2)

if resultado2 >= 6 : print('Aluno aprovado')
if resultado2 < 6 : print('Aluno reprovado')
