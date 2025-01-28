print('-=-' * 10)
while True: 
    nome = input('Digite seu nome: ')
    tamanho_nome = len(nome)
    if tamanho_nome < 4:
        print('Nome inválido, digite novamente')
    else:
        break
print('-=-' * 10)
while True:
    idade = int(input('Digite sua idade: '))
    if idade < 0 or idade > 150:
        print('Idade inválida, digite novamente')
    else:
        break
print('-=-' * 10)
while True: 
    salario = float(input('Digite seu salário: '))
    if salario < 0:
        print('Salário inválido, digite novamente')
    else:
        break
print('-=-' * 10)
while True:
    print('[f] - feminino\n[m] - masculino')
    sexo = input('Digite seu sexo: ').lower()
    if sexo != 'f' and sexo != 'm':
        print('Sexo inválido, digite novamente')
    else:
        break
print('-=-' * 10)
while True:
    print('[s] - solteiro\n[c] - casado\n[v] - viúvo\n[d] - divorciado')
    estado_civil = input('Digite seu estado civil: ').lower()
    if estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
        print('Estado civil inválido, digite novamente')
    else:
        break
print('-=-' * 10)
print('Fim do programa!')
