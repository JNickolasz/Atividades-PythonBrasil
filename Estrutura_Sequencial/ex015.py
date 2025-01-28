sal_hora = float(input('Quanto você ganha por hora? R$'))
horas_trab = int(input('Quantas horas você trabalha por mês? '))
sal_tot = sal_hora * horas_trab
print(f'Salário Bruto: R${sal_tot}.')
print(f'Imposto de Renda: R${sal_tot * 0.11}.')
print(f'INSS: R${sal_tot * 0.08}.')
print(f'Sindicato: R${sal_tot * 0.05}.')
print(f'Salário Líquido: R${sal_tot - (sal_tot * 0.11 + sal_tot * 0.08 + sal_tot * 0.05)}.')
