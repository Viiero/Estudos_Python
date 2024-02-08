#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganhoPorHora = float(input("Insira o valor que você ganha por hora: "))
horasTrabalhadas = float(input("Insira o número de horas trabalhadas no mês: "))

total = ganhoPorHora * horasTrabalhadas

print("O valor total do salário nesse mês é: R$", total)