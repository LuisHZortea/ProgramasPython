#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

b1 = float(input('Insira a nota do primeiro bimestre:''))
b2 = float(input('Insira a nota do segundo bimestre:''))
m = b1 + b2 / 2

if m > 7.0:
  print(f'Parabéns, você foi aprovado. Sua média foi {m}')
elif  7 > m >= 5.0:
  print(f'Você está de recuperação. Sua média foi {m}')
else:
  print(f'Você foi reprovado. Sua média foi {m}')
