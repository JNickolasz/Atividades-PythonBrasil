altura = float(input('Digite sua altura em metros:'))
print('''1. Homem
2. Mulher
''')
identidade = int(input('Escolha uma das opções: '))
if identidade == 1:
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é {peso_ideal:.2f}kg')
elif identidade == 2:
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é {peso_ideal:.2f}kg')
