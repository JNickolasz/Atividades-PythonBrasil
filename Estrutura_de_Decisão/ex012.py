salario_hora = int(input('Digite quanto você ganha por hora trabalhada: R$'))
hora = int(input('Digite a quantidade de horas que você trabalha: '))
salario_bruto = salario_hora * hora

if salario_bruto <= 900:
    print(f'Salário Bruto: R${salario_bruto}')
    ir = salario_bruto * 0
    print(f'IR: Isento')
    inss = salario_bruto * 0.1
    print(f'( - ) INSS (10%): R${inss}')
    fgts = salario_bruto * 0.11
    print(f'FGTS (11%): R${fgts}')
    total_descontos = ir + inss
    print(f'Total de descontos: R${total_descontos}')
    print(f'Salário Lìquido: R${salario_bruto - total_descontos}')
elif salario_bruto <= 1500:
    print(f'Salário Bruto: R${salario_bruto}')
    ir = salario_bruto * 0.05
    print(f'( - ) IR (5%): R${ir}')
    inss = salario_bruto * 0.1
    print(f'( - ) INSS (10%): R${inss}')
    fgts = salario_bruto * 0.11
    print(f'FGTS (11%): R${fgts}')
    total_descontos = ir + inss
    print(f'Total de descontos: R${total_descontos}')
    print(f'Salário Lìquido: R${salario_bruto - total_descontos}')

elif salario_bruto <= 2500:
    print(f'Salário Bruto: R${salario_bruto}')
    ir = salario_bruto * 0.1
    print(f'( - ) IR (10%): R${ir}')
    inss = salario_bruto * 0.1
    print(f'( - ) INSS (10%): R${inss}')
    fgts = salario_bruto * 0.11
    print(f'FGTS (11%): R${fgts}')
    total_descontos = ir + inss
    print(f'Total de descontos: R${total_descontos}')
    print(f'Salário Lìquido: R${salario_bruto - total_descontos}')
elif salario_bruto > 2500:
    print(f'Salário Bruto: R${salario_bruto}')
    ir = salario_bruto * 0.2
    print(f'( - ) IR (20%): R${ir}')
    inss = salario_bruto * 0.1
    print(f'( - ) INSS (10%): R${inss}')
    fgts = salario_bruto * 0.11
    print(f'FGTS (11%): R${fgts}')
    total_descontos = ir + inss
    print(f'Total de descontos: R${total_descontos}')
    print(f'Salário Lìquido: R${salario_bruto - total_descontos}')
