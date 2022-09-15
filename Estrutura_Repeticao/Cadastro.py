nome=input('Nome: ')
while len(nome)<3:
    nome=input('Nome deve conter mais que 3 caracteres: ')


idade=int(input('Idade: '))
while idade<0 or idade>150:
    idade=int(input('Idade entre 0 e 150 anos: '))


salario=float(input('Salário: '))
while salario<0:
    salario=float(input('Salário tem que ser maior que 0: '))


sexo=input('Sexo: ')
while sexo!='F' and sexo!='M':
    sexo=input('F ou M: ')

estado_civil=input('Estado Civil: ')
while estado_civil!='S' and estado_civil!='C' and estado_civil!='V' and estado_civil!='D':
    estado_civil=input('S, C, V ou D: ')