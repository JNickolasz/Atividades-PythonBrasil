while True: 
    nome: str = input('Digite o nome: ').upper()
    senha: str = input('Digite a senha: ').upper()
    if nome == senha:
        print('Nome e senha não podem ser iguais!')
        print('Tente novamente!')
    else:
        print('Nome e senha diferentes!')
        break

print('Fim do programa!')
