#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite seu nome completo: ').strip()
d = nome.split()
print('Seu primeiro nome é: {}'.format(d[0]))
print('Seu último nome é: {}'.format(d[len(d)-1]))
