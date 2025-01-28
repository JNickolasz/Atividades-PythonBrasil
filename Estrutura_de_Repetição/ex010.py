n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n2 > n1: 
    for i in range (n2, n1):
        print(i)
elif n1 > n2:
    for i in range (n1, n2, -1):
        print(i)
elif n1 == n2: 
    print('Os números são iguais, não há intervalo!')
