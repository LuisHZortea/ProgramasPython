#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
nome = input('Me diga seu nome: ')
print('Seu nome em maiusculo é:',nome.upper())
print('Seu nome em minusculo é:',nome.lower())
print(len(nome) - nome.count(' '))
print(nome.find(' '))
