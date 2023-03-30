#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

p = float(input('Preço das compras: '))

print('FORMAS DE PAGAMENTO:')
print('[1] à vista dinheiro/cheque')
print('[2] à vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
o = int(input('Qual a opção? '))

if o == 1:
  v = p - (p * 10 / 100)
  print(f'O valor a ser pago será {v}.')
elif o == 2:
  v = p - (p * 5 / 100)
  print(f'O valor a ser pago será {v}.')
elif o == 3:
  p = p / 2
  print(f'O valor a ser pago são 2 parcelas de {p}.')
else:
  v = p + (p * 20 / 100)
  totalpar = int(input('Quantas parcelas? '))
  v1 = v / totalpar
  print(f'O valor a ser pago serão {totalpar} parcelas de {v1}.')
