# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
cont = 0
s = 0
for c in range(1, 501, 2):
  if c % 3 == 0:
    s += c
    cont = cont + 1
print(f'A somatória dos números que são múltiplos de três e se encontram no intervalo é {s}. Foram solicitados {cont} números.')
