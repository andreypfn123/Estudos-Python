valor_hora=float(input('Quanto recebe por hora: '))
mes_hora=float(input('Horas trabalhadas no mês: '))
salario_bruto=valor_hora*mes_hora
if salario_bruto <= 900:
    print(f'Salário Bruto: R${salario_bruto:,.2f}\
        \n(-) IR: Isento do imposto de renda\
        \n(-) INSS (10%): R${salario_bruto*0.10:,.2f}\
        \nFGTS (11%): R${salario_bruto*0.11:,.2f}\
        \nTotal de descontos: R${(salario_bruto*0.10):,.2f}\
        \nSalário Líquido: R${salario_bruto-(salario_bruto*0.10):,.2f}')
elif salario_bruto <= 1500:
    print(f'Salário Bruto: R${salario_bruto:,.2f}\
        \n(-) IR (5%): R${salario_bruto*0.05:,.2f}\
        \n(-) INSS (10%): R${salario_bruto*0.10:,.2f}\
        \nFGTS (11%): R${salario_bruto*0.11:,.2f}\
        \nTotal de descontos: R${(salario_bruto*0.05)+(salario_bruto*0.10):,.2f}\
        \nSalário Líquido: R${salario_bruto-(salario_bruto*0.05)-(salario_bruto*0.10):,.2f}')
elif salario_bruto <= 2500:
    print(f'Salário Bruto: R${salario_bruto:,.2f}\
        \n(-) IR (10%): R${salario_bruto*0.10:,.2f}\
        \n(-) INSS (10%): R${salario_bruto*0.10:,.2f}\
        \nFGTS (11%): R${salario_bruto*0.11:,.2f}\
        \nTotal de descontos: R${(salario_bruto*0.10)+(salario_bruto*0.10):,.2f}\
        \nSalário Líquido: R${salario_bruto-(salario_bruto*0.10)-(salario_bruto*0.10):,.2f}')
elif salario_bruto > 2500:
    print(f'Salário Bruto: R${salario_bruto:,.2f}\
        \n(-) IR (20%): R${salario_bruto*0.20:,.2f}\
        \n(-) INSS (10%): R${salario_bruto*0.10:,.2f}\
        \nFGTS (11%): R${salario_bruto*0.11:,.2f}\
        \nTotal de descontos: R${(salario_bruto*0.20)+(salario_bruto*0.10):,.2f}\
        \nSalário Líquido: R${salario_bruto-(salario_bruto*0.20)-(salario_bruto*0.10):,.2f}')