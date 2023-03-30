#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice #de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

while True:
  try:
    print('Vamos calcular o IMC.')
    m = float(input('Informe sua massa (em kg): '))
    if m <= 0:
      print('\nValor inválido. Tente novamente.\n')
    else:
      break
  except:
    print('\nDado inválido. Tente novamente.\n')

while True:
  try:
    a = float(input('Informe sua altura (em metros): '))
    if a <= 0:
      print('\nValor inválido. Tente novamente.\n')
    else:
      break
  except:
    print('\nDado inválido. Tente novamente.\n')

imc = m / pow(a, 2)
print(f'Seu IMC é: {imc :.1f}')
if imc < 18.5:
  print('Abaixo do peso.')
elif 18.5 < imc <= 25:
  print('Peso ideal.')
elif 25 < imc <= 30:
  print('Sobrepeso.')
elif 30 < imc <= 40:
  print('Obesidade.')
else:
  print('Obesidade mórbida.') 
