#Crie um programa que faça o computador jogar Jokenpô com você.
while True:
  try:
    print('Escolha:')
    print('''[1] Pedra
[2] Papel
[3] Tesoura''')
    j = int(input('Sua escolha: '))
    if 0 >= j < 3:
      print('\nValor inválido. Tente novamente.\n')
    else:
      break
  except:
    print('\nDado inválido. Tente novamente.\n')
    
c = randint(1,3)
print(f'Escolha do computador: {c}')

if j == 1 and c == 2:
  print('Computador vence.')
elif j == 1 and c == 3:
  print('Jogador vence.')
elif j == 2 and c == 1:
  print('Jogador vence.')
elif j == 2 and c == 3:
  print('Computador vence.')
elif j == 3 and c == 1:
  print('Computador vence.')
elif j == 3 and c == 2:
  print('Jogador vence.')
else:
  print('Empate.')
