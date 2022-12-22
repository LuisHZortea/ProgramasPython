#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
ang = int(input('Digite o valor de um ângulo: '))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print(f'O seno, cosseno, e tangente desse ângulo são respectivamente: {s:.2f}, {c:.2f}, {t:.2f}')
