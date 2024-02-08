#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

h = float(input("Altura: "))

pHomem = (72.7 * h) - 58
pMulher = (62.1 * h) - 44.7

print("Peso ideal para homem: \n", pHomem, "Peso ideal para mulher: ", pMulher)