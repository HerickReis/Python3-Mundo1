print('Olá seja bem-vindo ao nosso programa de calculo de descontos!')
produto = float(input('Qual valor do produto?: '))
desconto = float(input('Valor do desconto: '))
descontoR = produto - (produto * desconto/100) 
print(f'O valor do produto com desconto é {descontoR:.2f}!')