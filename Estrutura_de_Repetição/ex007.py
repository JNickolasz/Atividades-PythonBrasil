"""Saber qual o maior dos números digitados pelo usuário usando if e else."""
while  True:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))
    n4 = int(input('Digite o quarto número: '))
    n5 = int(input('Digite o quinto número: '))
    maior = n1  
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    if n4 > maior:
        maior = n4
    if n5 > maior:
        maior = n5
    print(f'O maior número digitado foi {maior}.')
print('-=-' * 10)
