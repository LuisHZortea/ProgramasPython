#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de #triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

while True:
  try:
    A = float(input('Insira o valor do lado A: '))
    if A < 0:
      print('\nValor inválido. Tente novamente.\n')
    else:
      break
  except:
    print('\nDado inválido. Tente novamente.\n')

while True:
  try:
    B = float(input('Insira o valor do lado B: '))
    if B < 0:
      print('\nValor inválido. Tente novamente.\n')
    else:
      break
  except:
    print('\nDado inválido. Tente novamente.\n')

while True:
  try:
    C = float(input('Insira o valor do lado C: '))
    if C < 0:
      print('\nValor inválido. Tente novamente.\n')
    else:
      break
  except:
    print('\nDado inválido. Tente novamente.\n')

if A < B + C and B < A + C and C < A + B:
   print('Os valores formam um triângulo.')

if A == B == C:
  print('Triângulo Equilátero.')

if A == B and A == C or B == C and B == A:
  print('Triângulo Isóceles.')

if A != B != C:
  print('Triângulo Escaleno.')
