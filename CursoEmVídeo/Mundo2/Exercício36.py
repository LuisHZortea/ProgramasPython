#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

c = int(input('Qual o valor da casa? '))
s = float(input('Qual é o seu salário? '))
a = int(input('Em quantos anos você vai pagar? '))

pm = c / (a * 12)
ex = (30 * s) / 100

print(f'Para pagar uma casa no valor de R${c} em {a} anos, a prestação mensal será no valor de R${pm}.')
if pm <= ex:
  print('Empréstimo concedido! Você pode comprar essa casa.')
else:
  print('Empréstimo negado! Infelizmente você não pode comprar essa casa. ')
