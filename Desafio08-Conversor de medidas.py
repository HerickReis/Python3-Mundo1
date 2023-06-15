distancia = float(input ('Digite uma distancia em metros: '))
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000
dam = distancia / 10
hm = distancia  / 100
km = distancia  / 1000
print(f'{distancia} metros equivale a {km:.3f} quiilometros, {hm:.2f} Hectômetro, {dam:.2f} Decâmetros \n E {mm:.0f} Milimetros, {cm:.0f} centímetros, {dm:.0f} Decímetro.')