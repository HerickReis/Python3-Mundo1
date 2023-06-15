'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''
n = int(input('Digite um número inteiro: '))
if n % 2 == 0:  # se a variável n tiver o valor do resto da divisão igual a 0 o número será par
    print('\x1b[32mO número é par')

else: # caso contrário ele será ímpar
    print('\x1b[31mo número é ímpar')
    