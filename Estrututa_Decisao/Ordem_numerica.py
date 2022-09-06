num1=int(input('Diga o primeiro número: '))
num2=int(input('Diga o segundo número: '))
num3=int(input('Diga o terceiro número: '))
lista=[num1,num2,num3]
lista.sort(reverse=True)
print('Ordem decrescente:',lista)
lista.sort()
print('Ordem crescente:',lista)