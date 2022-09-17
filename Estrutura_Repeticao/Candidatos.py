possiveis_votos = [1, 2, 3, 4, 5, 6]
candidatos = ['Ciro Gomes', 'Jair Bolsonaro', 'João Amoedo', 'Lula Molusco', 'Nulo', 'Branco']
votos=[]
n_votos=1
voto = True
while voto!=0:
    print('Voto número', n_votos)
    voto=int(input('Digite o seu voto: '))
    if voto == 0:
        break
    else:
        while voto not in possiveis_votos:
            print('Voto inválido')
            voto=int(input('Digite o seu voto: '))
        votos.append(voto)
    n_votos+=1

contador=0
for i in range(len(candidatos)):
    print('Votos para', candidatos[contador], end=': ')
    if votos.count==0:
        print('0')
        contador+=1
    else:
        print(votos.count(contador+1))
        contador+=1

porc_nulo=(votos.count(5)/len(votos))*100
porc_branco=(votos.count(6)/len(votos))*100
print(f'Porcentagem Nulos: {porc_nulo:.2f}%\
    \nPorcentagem Brancos: {porc_branco:.2f}%')