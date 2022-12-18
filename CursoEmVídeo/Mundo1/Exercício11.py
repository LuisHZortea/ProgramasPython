#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
l = float(input("Informe a largura da parede: "))
al = float(input("Informe a altura da parede:"))
a = (l * al)
t = a / 2
print("Para pintar a parede de {} m², precisará de {} litros de tinta.".format(a, t))
