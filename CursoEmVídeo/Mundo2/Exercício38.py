#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

if n1 > n2:
  print(f'O primeiro valor inserido, no caso {n1}, é maior do que o segundo.')
elif n2 > n1:
  print(f'O segundo valor inserido, no caso {n2} é maior do que o primeiro.')
else:
  print('Os dois valores são iguais.')
