voto=int(input(' João = 1\
    \nMaria = 2\
    \nLucas = 3\
    \nCarlos = 4\
    \nVoto Nulo = 5\
    \nVoto em Branco = 6\
    \nPara finalizar = 0\
    \nDigite o número do voto: '))
while voto!=0:
    voto=int(input('Próximo voto: '))
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