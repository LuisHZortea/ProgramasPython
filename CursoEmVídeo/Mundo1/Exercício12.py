#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = int(input("Informe o preço do produto: "))
np = p - (p * 0.05)
print("O produto com 5% de desconto sairá por: {} ".format(np))
