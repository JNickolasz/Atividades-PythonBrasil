n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
#Imprima os números em ordem decrescente

if n1 > n2 and n1 > n3:
    a = n1
    if n2 > n3:
        b = n2
        c = n3
    else:
        b = n3
        c = n2

elif n2 > n1 and n2 > n3:
    a = n2
    if n1 > n3:
        b = n1
        c = n3
    else:
        b = n3
        c = n1

elif n3 > n1 and n3 > n2:
    a = n3
    if n1 > n2:
        b = n1
        c = n2
    else:
        b = n2
        c = n1

print(f'Os números em ordem decrescente são: {a}, {b}, {c}.')
