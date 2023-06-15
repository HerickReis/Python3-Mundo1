''' Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.'''
from datetime import date
a = int(input('Qual o ano? Coloque 0 para analisar o ano atual '))
if a == 0:
    a =date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 : # se o valor da variável a tiver o valor do resto da divisão igual a 0 o ano será bissexto.
    print(f'O ano {a} é bissexto')
else: # caso contrário não será bissexto.
    print(f'O ano {a} não é bissexto')