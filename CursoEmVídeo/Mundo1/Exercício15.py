#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos km foram percorridos? '))
d = int(input('Por quantos dias o carro foi utilizado? '))
v = (60 * d) + (0.15 * km)
print('O preço a pagar por {} km rodados e {} dias utilizados é {:.2f}'.format(km, d, v))
