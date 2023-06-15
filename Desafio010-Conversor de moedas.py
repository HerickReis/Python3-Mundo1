print('Olá seja bem-vindo ao nosso Conversor de Moedas')
Real = float(input('Qual valor a ser convertido ? R$ '))
Euro = Real / 5.58
Dolar = Real / 5.23
LibraEsterlina = Real / 6.27
yene = Real * 25.68
RialCatarino = Real /1.44
print(f' {Real} Reais \n vale :\n {Euro:.2f} Euro/s \n {Dolar:.2f} Dolar/es \n {LibraEsterlina:.2f} Libra/s \n {yene:.2f} Yenes \n {RialCatarino:.2f} Rial/is')