vogais = 'a', 'e', 'i', 'o', 'u'
letra = input('Digite uma letra: ')

if letra in vogais:
    print('A letra é uma vogal.')

elif letra not in vogais: 
    print('A letra é uma consoante.')
