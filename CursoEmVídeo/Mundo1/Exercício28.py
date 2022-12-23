#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
ns = randint(0, 5)
ne = int(input('Qual número estou pensando? '))
if ne == ns:
  print('Parabéns, você acertou!')
else:
  print(f'Uma pena, você errou! Eu pensei no número {ns}')
