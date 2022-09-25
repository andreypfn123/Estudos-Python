pais_a=80000
pais_b=200000
anos=0
taxa_crescimento=1.5
while pais_a<=pais_b:
    pais_a+=pais_a*0.03
    pais_b+=pais_b*0.015
    anos+=1
print(f'O Pais A ultrapassa o Pais B em {anos} anos')