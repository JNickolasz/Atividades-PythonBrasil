print('-=-' * 10)
contador = 0
while True:
    contador += 1
    print(f'=-=-=-Operação número {contador}.-=-=-=')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))
    n4 = int(input('Digite o quarto número: '))
    n5 = int(input('Digite o quinto número: '))
    soma = n1 + n2 + n3 + n4 + n5
    media = soma / 5
    print(f'A soma dos números digitados é {soma} e a média é {media:.2f}.')
    print('-=-' * 10)
