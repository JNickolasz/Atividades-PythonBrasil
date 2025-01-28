while True:
    nota = int(input('Digite a nota: '))
    if nota >= 0 and nota <= 10:
        print('Nota válida!')
    else:
        print('Nota inválida!')
        break

print('Fim do programa!')