'''um professor que sorteam um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.'''
from random import choice 
a1 = input('Qual o nome do primeiro aluno? ')
a2 = input('Qual o nome do segundo aluno? ')
a3 = input('Qual o nome do terceiro aluno? ')
a4 = input('Qual o nome do quarto aluno ? ')
print(f'Parabéns o aluno {choice([a1, a2, a3, a4]):=^10} foi escolhido')