n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}')
    
    if n2 < n3:
        print(f'O menor número é {n2}')
    elif n3 < n2: 
        print(f'O menor número é {n3}.')

elif n2 > n1 and n2 > n3: 
    print(f'O maior número é {n2}.')
    
    if n1 > n2: 
        print(f'O menor número é {n2}.')
    elif n2 > n1: 
        print(f'O menor número é {n1}.')

elif n3 > n1 and n3 > n2: 
    print(f'O maior número é {n3}.')

    if n2 > n1: 
        print(f'O menor número é {n1}.')
    elif n1 > n2:
        print(f'O menor número é {n2}.')
