#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Qual o seu nome completo? ')).strip()
s = nome[:].upper()
print('Seu nome tem Silva? {}'.format('SILVA' in s))
