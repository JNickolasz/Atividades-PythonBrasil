print('-=-' * 12)
print('M - Matutino\nV - Vespertino\nN - Noturno')
turno = input('Informe em que turno você estuda? ')

if turno == 'M' or turno == 'm':
    print('Bom dia!')

elif turno == 'V' or turno == 'v':
    print('Boa tarde!')

elif turno == 'N' or turno == 'n': 
    print('Boa noite!')

else: 
    print('Valor inválido. Tente novamente.')

print('-=-' * 12)
