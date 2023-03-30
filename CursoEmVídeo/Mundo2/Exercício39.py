#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

nasc = int(input('Insira seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade < 18:
  print(f'Ainda faltam {18-idade} anos para seu alistamento.')
elif idade > 18:
  print(f'Já passou o tempo de se alistar. Você está atrasado {idade-18} ano(s).')
else:
  print('Você tem que se alistar nesse ano.')
