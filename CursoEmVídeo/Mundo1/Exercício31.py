#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
d = float(input('Qual é a distância que será percorrida na viagem? '))
if d <= 200:
  v = d * 0.5
else:
  v = d * 0.45
print(f'O valor que deverá ser pago é R${v}')
