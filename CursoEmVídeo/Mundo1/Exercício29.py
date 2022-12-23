#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v = float(input('Qual é a velocidade atual do carro? '))
m = (v-80) * 7.0 
if v > 80:
  print(f'Rápido demais, terei que te multar. O valor da sua multa é: R$ {m}')
print('Tudo certo. Siga em paz.')
