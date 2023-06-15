print('Olá seja bem-vindo ao programa de média aritmética')

nome = input('Qual nome do Aluno?: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

soma = n1 + n2

média = soma / 2

if média <7.0:
    print (f'a média foi de {média} e infelizmente aluno {nome} foi retido :(')

else : 
      print (f'UAU! a média foi de {média} e o aluno {nome} foi aprovado :)')