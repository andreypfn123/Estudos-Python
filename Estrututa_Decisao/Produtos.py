produto1=float(input('Diga o valor do primeiro produto: '))
produto2=float(input('Diga o valor do segundo produto: '))
produto3=float(input('Diga o valor do terceiro produto: '))
menor=produto1
if produto1<produto2 and produto1<produto3:
    print('Você deve comprar o primeiro produto que custa R$%.2f'%produto1)
if produto2<produto1 and produto2<produto3:
    print('Você deve comprar o segundo produto que custa R$%.2f'%produto2)
if produto3<produto1 and produto3<produto2:
    print('Você deve comprar o terceiro produto que custa R$%.2f'%produto3)