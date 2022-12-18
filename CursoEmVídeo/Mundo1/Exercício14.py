#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Digite uma temperatura em °C para converter: '))
f = (c * 1.8) + 32
print('{} graus celsius são {} graus Fahrenheit.'.format(c, f))
