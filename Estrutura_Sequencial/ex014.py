peso = int(input('Digite o peso total de peixes: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print('''O peso é maior que o estabelecido pelo regulamento \nde pesca do estado de São Paulo (50 quilos).\nVocê deve pagar uma multa de R$ 4,00 por quilo excedente!!''')
    print(f'O peso excedente é de {excesso}kg e a multa a ser paga é de R${multa:.2f}')

elif peso <= 50:
    print('O peso está dentro do permitido pelo regulamento de pesca. Não há multa a ser paga!')
