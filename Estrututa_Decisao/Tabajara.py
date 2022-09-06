salario=float(input('Digite seu salário: '))
if salario<=280:
    print(f'Salário antes R${salario:,.2f}, aumento de 20% = R${salario*0.20:,.2f}, salário atual = R${(salario*0.20)+salario:,.2f}')
elif salario>280 and salario<=700:
    print(f'Salário antes R${salario:,.2f}, aumento de 15% = R${salario*0.15:,.2f}, salário atual = R${(salario*0.15)+salario:,.2f}')
elif salario>700 and salario<=1500:
    print(f'Salário antes R${salario:,.2f}, aumento de 10% = R${salario*0.10:,.2f}, salário atual = R${(salario*0.10)+salario:,.2f}')
elif salario>1500:
    print(f'Salário antes R${salario:,.2f}, aumento de 5% = R${salario*0.05:,.2f}, salário atual = R${(salario*0.05)+salario:,.2f}')