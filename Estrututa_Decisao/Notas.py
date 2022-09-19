nota1=float(input('Primeira nota: '))
nota2=float(input('Segunda nota: '))
nota3=float(input('Terceira nota: '))
media=(nota1+nota2+nota3)/3
if media>=7 and media<10:
    print(f'Média {media:.2f} \
        \nAprovado')
elif media<7:
    print(f'Média {media:.2f}\
        \nReprovado')
elif media==10:
    print(f'Média {media:.2f}\
        \nAprovado com Distinção')