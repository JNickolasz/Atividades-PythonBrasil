contador = 0
populacao_A = int(input('Digite a população do país A: '))
populacao_B = int(input('Digite a população do país B: '))
taxa_A = int(input('Digite a taxa de crescimento da população do país A em porcentagem: '))
taxa_B = int(input('Digite a taxa de crescimento da população do país B em porcentagem: '))

while True:
    populacao_A += populacao_A * (taxa_A / 100)
    populacao_B += populacao_B * (taxa_B / 100)
    print('-=-' * 10)
    print('População do país A:', populacao_A)
    print('Ano:', contador + 1) 
    print('População do país B:', populacao_B)
    print('Ano:', contador + 1)
    print('-=-' * 10)
    contador += 1
    
    if populacao_A > populacao_B:
        print('O país A ultrapassou o país B em', contador, 'anos')
        break
    