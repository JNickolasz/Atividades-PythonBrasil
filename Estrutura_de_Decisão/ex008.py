preco_1 = float(input('Informe o preço do primeiro produto: R$'))
preco_2 = float(input('Informe o preço do segundo produto: R$'))
preco_3 = float(input('Informe o preço do terceiro produto: R$'))

if preco_1 < preco_2 and preco_1 < preco_3:
    print(f'O produto mais barato é o primeiro, custando R${preco_1:.2f}.')

elif preco_2 < preco_1 and preco_2 < preco_3:
    print(f'O produto mais barato é o segundo, custando R${preco_2:.2f}.')

elif preco_3 < preco_1 and preco_3 < preco_2:
    print(f'O produto mais barato é o terceiro, custando R${preco_3:.2f}.')

elif preco_1 == preco_2 and preco_1 == preco_3:
    print(f'Todos os produtos custam o mesmo preço, R${preco_1:.2f}.')
