'''Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule e peça o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R#0,45 para viagens mais longas.'''
from time import sleep
distancia = float(input('Qual a distância da viagem? '))
print('\x1b[36mCalculando...')
sleep(1.2)
if distancia <= 200: # se a distancia for igual ou menor que 200 km/s o valor será por km será de R$ 0.50
    print(f'\x1b[35mO valor da passagem para {distancia}kms é de R$: {distancia *0.50:.2f}')

else: # se a distância for maior que 200 km/s o valor será de R$ 0.45
    print(f'\x1b[35mO valor da passagem para {distancia}kms é de R$: {distancia * 0.45:.2f}')