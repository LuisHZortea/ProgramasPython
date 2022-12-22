#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
num = float(input('Digite um número: '))
print('A parte inteira do número é: {}'.format(math.trunc(num)))
