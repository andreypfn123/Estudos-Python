nota1=float(input('Primeira nota: '))
nota2=float(input('Segunda nota: '))
media=(nota1+nota2)/2
if media >=9.0 and media <= 10:
    print (f'Nota 1 = {nota1}\
        \nNota 2 = {nota2}\
        \nMédia = {media}\
        \nConceito = A\
        \nAprovado')
elif media >=7.5 and media <= 9.0:
    print(f'Nota 1 = {nota1}\
        \nNota 2 = {nota2}\
        \nMédia = {media}\
        \nConceito = B\
        \nAprovado')
elif media >= 6.0 and media <=7.5:
    print(f'Nota 1 = {nota1}\
        \nNota 2 = {nota2}\
        \nMédia = {media}\
        \nConceito = C\
        \nAprovado')
elif media >= 4.0 and media <= 6.0:
    print(f'Nota 1 = {nota1}\
        \nNota 2 = {nota2}\
        \nMédia = {media}\
        \nConceito = D\
        \nReprovado')
elif media >= 0 and media <= 4.0:
    print(f'Nota 1 = {nota1}\
        \nNota 2 = {nota2}\
        \nMédia = {media}\
        \nConceito = E\
        \nReprovado')
