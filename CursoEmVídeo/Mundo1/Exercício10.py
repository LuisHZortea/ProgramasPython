#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
r = float(input("Quantos dinheiro você tem na carteira?R$ "))
c = r / 3.27
print("Com R${:.2f} você pode comprar US${:.2f}.".format(r, c))
