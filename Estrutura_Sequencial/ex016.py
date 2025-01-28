tamanho = int(input('Digite o tammanho em metros quadrados da área a ser pintada: '))
print('Você quer comprar galões de 3,6 litros ou latas de 18 litros?')
print('1 - Galões')
print('2 - Latas')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    galao = 3.6
    if tamanho % 3.6 == 0:
        latas = tamanho // 3.6
    else:
        latas = tamanho // 3.6 + 1
    print(f'Você precisará de {latas} galão(ões) de tinta')
    print(f'Valor total: R$ {latas * 25}')
elif opcao == 2:
    lata = 18
    if tamanho % 18 == 0:
        latas = tamanho // 18
    else:
        latas = tamanho // 18 + 1
    print(f'Você precisará de {latas} lata(s) de tinta')
    print(f'Valor total: R$ {latas * 80}')
else:
    print('Opção inválida')
    