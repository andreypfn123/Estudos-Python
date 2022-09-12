import math

valor_a=float(input('Diga o valor de a: '))
if valor_a == 0:
    print('Não é segundo grau.')
else:
    valor_b=float(input('Diga o valor de b: '))
    valor_c=float(input('Diga o valor de c: '))
    delta=valor_b*valor_b-(4*valor_a*valor_c)
print(delta)