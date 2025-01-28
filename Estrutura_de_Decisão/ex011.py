salario = float(input('Digite seu salário: R$'))
if salario <= 280: 
    novo_salario = salario + (salario * 0.2)
    print(f'Salário antes do reajuste: R${salario:.2f}')
    print(f'Percentual de aumento aplicado: 20%')
    print(f'Valor do aumento: R${salario * 0.2:.2f}')
    print(f'Novo salário: R${novo_salario:.2f}')

elif salario > 280 and salario <= 700:
    novo_salario = salario + (salario * 0.15)
    print(f'Salário antes do reajuste: R${salario:.2f}')
    print(f'Percentual de aumento aplicado: 15%')
    print(f'Valor do aumento: R${salario * 0.15:.2f}')
    print(f'Novo salário: R${novo_salario:.2f}')

elif salario > 700 and salario <= 1500:
    novo_salario = salario + (salario * 0.1)
    print(f'Salário antes do reajuste: R${salario:.2f}')
    print(f'Percentual de aumento aplicado: 10%')
    print(f'Valor do aumento: R${salario * 0.1:.2f}')
    print(f'Novo salário: R${novo_salario:.2f}')

else:
    novo_salario = salario + (salario * 0.05)
    print(f'Salário antes do reajuste: R${salario:.2f}')
    print(f'Percentual de aumento aplicado: 5%')
    print(f'Valor do aumento: R${salario * 0.05:.2f}')
    print(f'Novo salário: R${novo_salario:.2f}')

