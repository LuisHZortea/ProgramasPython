#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

n1 = int(input("Digite um número: "))
print("O dobro, o triplo, e a raíz quadrada de {} são respectivamente: {}, {}, {}. ".format(n1, (n1*2), (n1*3), (math.sqrt(n1))))
