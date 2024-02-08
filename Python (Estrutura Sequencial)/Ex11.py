#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

num1 = float(input("Digite um número inteiro: "))
num2 = float(input("Digite outro número inteiro: "))
num3 = float(input("Agora digite um número real: "))

calc1 = (2 * num1) * (num2/2)
calc2 = (3 * num1) + num3
calc3 = num3**3

print("O produto do dobro do primeiro com metade do segundo é: ", calc1, "a soma do triplo do primeiro com o terceiro: ", calc2, "O terceiro elevado ao cubo: ", calc3)

