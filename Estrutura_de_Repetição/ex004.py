contador = 0
populacao_paisA = 80000 
populacao_paisB = 200000
while True: 
    print('-=-' * 10)
    print('População do país A:', populacao_paisA)
    print('Ano:', contador + 1) 
    print('População do país B:', populacao_paisB)
    print('Ano:', contador + 1)
    print('-=-' * 10)
    populacao_paisA += populacao_paisA * 0.03
    populacao_paisB += populacao_paisB * 0.015
    contador += 1
    

    if populacao_paisA > populacao_paisB:
        print('O país A ultrapassou o país B em', contador, 'anos')
        break
