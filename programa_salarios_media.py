idades = [35,32,50,33,48,50,33,48,22,49,35,38,20,47,49,48,34,21,48,44,48,30,25,42,42,23,25,23,38,35]
salarios = [3739,2219,3554,3978,4014,3270,4792,3879,2981,2384,4826,2460,3680,4318,1872,1770,4640,3929,3295,1729,
            3965,4267,4007,1916,2987,2943,3852,4543,2055,1730]

qnt_salarios = 30
soma_salarios = sum(salarios)
media = soma_salarios / qnt_salarios

qnt_funcionarios = 0
qnt_funcionarios2 = 0

for i, idade in enumerate(idades):
    if idade > 25 and salarios[i] <= media:
        qnt_funcionarios += 1
        #print(idades[i])
        #print(salarios[i])
print()
print(f'A quantidade de funcionarios com mais de 25 anos e recebem salarios abaixo da média são: {qnt_funcionarios}')

for i, idade in enumerate(idades):
    if salarios[i] >= media:
        qnt_funcionarios2 += 1
        #print(idades[i])
        #print(salarios[i])

print(f'A quantidade de funcionarios que recebem salarios na média são: {qnt_funcionarios2}')