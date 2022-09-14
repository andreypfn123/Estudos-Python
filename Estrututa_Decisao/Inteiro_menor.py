numero=int(input('Digite um número positivo menor que 1000: '))
unidade=numero%10
dezena=numero%10
centena=numero
numero=(numero-unidade)/10
numero=(numero-dezena)/10
print(f'{centena} centena(s),{dezena} dezena(s), {unidade} unidade(s)')