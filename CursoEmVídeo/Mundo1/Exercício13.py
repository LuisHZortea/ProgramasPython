#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input("Informe o salário do funcionário: "))
ns = s + (s * 0.15)
print("O novo salário com 15% de aumento é {}".format(ns))
