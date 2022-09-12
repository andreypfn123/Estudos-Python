lado1=float(input('Diga o primeiro lado do triângulo: '))
lado2=float(input('Diga o segundo lado do triângulo: '))
lado3=float(input('Diga o terceiro lado do triângulo: '))
if lado1+lado2<lado3 or lado1+lado3<lado2 or lado2+lado3<lado1:
    print('Não é um triângulo')
elif lado1 == lado2 and lado1 == lado3:
    print('Equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Isósceles')
else:
    print('Escaleno')