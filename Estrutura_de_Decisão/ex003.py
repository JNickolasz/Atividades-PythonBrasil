print('F - Feminino\nM- Masculino')
sexo = input('Escolha seu sexo: ').upper()

if sexo == 'M':
    print('Você selecionou o sexo masculino.')

elif sexo == 'F':
    print('Você selecionou o sexo feminino.')

else: 
    print('Sexo inválido.')
