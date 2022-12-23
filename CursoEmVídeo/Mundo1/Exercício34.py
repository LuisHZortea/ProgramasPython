#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Qual o salário do funcionário: '))
if s >= 1250:
  a = (s * 0.10) + s
else:
  a = (s * 0.15) + s
print(f'O novo salário será {a}.')
