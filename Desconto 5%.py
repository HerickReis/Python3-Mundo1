produto = float(input('Qual valor do Produto ? R$:'))
desconto = produto - (produto * 5/100) 
print(f'O produto que custava R${produto}, na promoção de 5% custa {desconto}')