salario = float(input('Qual era o valor antes do aumento ? R$ '))
reajuste = float(input('Qual será o aumento ? '))
aumento = salario + (salario * reajuste/100)
print (f'o salario era de {salario}, agora com o aumento passará a ser {aumento:.1f}')