voto=int(input(' João = 1\
    \n Maria = 2\
    \n Lucas = 3\
    \n Carlos = 4\
    \n Voto Nulo = 5\
    \n Voto em Branco = 6\
    \n Para finalizar = 0\
    \n Digite o número do voto: '))
while voto==0:
    voto=int(input('Digite um número válido: '))
candidato1=0
candidato2=0
candidato3=0
candidato4=0
nulo=0
branco=0
if voto == 1:
    candidato1=candidato1+1
if voto == 2:
    candidato2=candidato2+1
if voto == 3:
    candidato3=candidato3+1
if voto == 4:
    candidato4=candidato4+1
if voto == 5:
    nulo=nulo+1
if voto == 6:
    branco=branco+1
print(candidato1)