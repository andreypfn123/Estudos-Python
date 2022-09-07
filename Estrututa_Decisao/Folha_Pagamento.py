valor_hora=float(input('Quanto recebe por hora: '))
mes_hora=float(input('Horas trabalhadas no mês: '))
salario_bruto=valor_hora*mes_hora
if salario_bruto <= 900:
    print('Isento de imposto de renda')
elif salario_bruto <= 1500:
    print(f'Salário Bruto: R${salario_bruto}\n(-) IR (5%): R${salario_bruto*0.05}\n(-) INSS (10%): R${salario_bruto*0.11}')
elif salario_bruto <= 2500:
    print()
elif salario_bruto > 2500:
    print('Salário Bruto: R$\n(-) IR')