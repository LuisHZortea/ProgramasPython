#A Confederação Nacional de Natação precisa de um programa que leia o ano de #nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date

nasc = int(input("Insira o seu ano de nascimento: "))
ano = date.today().year
i = ano - nasc

if i <= 9:
  print('Mirim.')
elif 9 < i <= 14:
  print('Infantil.')
elif 14 < i <= 19:
  print('Júnior.')
elif 19 < i <= 25:
  print('Sênior.')
else:
  print('Master.')
