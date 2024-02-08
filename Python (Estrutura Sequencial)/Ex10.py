#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

from fractions import Fraction

frac1 = Fraction(9, 5)

C = float(input("Qual a temperatura? (em graus Celsius): "))

F = frac1 * C + 32

print("A temperatura em Fahrenheit é: ", F)