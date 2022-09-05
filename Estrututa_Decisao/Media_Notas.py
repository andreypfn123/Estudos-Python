nota=int(input('Digite aqui sua primeira nota: '))
nota2=int(input('Digite aqui sua segunda nota: '))
media=(nota+nota2)/2
if media<7:
    print('Reprovado')
elif media>=7 and nota <10:
    print('Aprovado')
elif media>=10:
    print('Aprovado com Distinção')