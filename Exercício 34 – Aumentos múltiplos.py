''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. -Para salários superiores a R$1.250,00, calcule um aumento de 10%. 
-Para os inferiores ou iguais, o aumento é de 15%.'''
from time import sleep
salario = float(input('Qual seu salário atual? '))# input está pedindio que o usuário insira o salario atual
print('Calculando...') 
sleep(1.2)
if salario <= 1250.00: # se o salário for igual ou inferior a 1250.00 reais o ajuste será de 15 %
    
    print(f'seu aumento é de 15% então seu novo salário será de R$: {salario + (salario * 15 / 100):.2f}') # :.2f estou formatando o valor para axibir apenas duas casas após o ponto flutuante

else :  # se for maior que 1250.00 o ajuste será de 10 %
    print(f'seu aumento é de 10% então seu novo salário será de R$: {salario + (salario * 10 / 100):.2f}')