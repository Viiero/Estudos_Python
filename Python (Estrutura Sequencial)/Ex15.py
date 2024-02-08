#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

valorPorHora = float(input("Informe o valor ganho por hora: "))
horasTrabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))

# Salário Bruto
salarioBruto = valorPorHora * horasTrabalhadas

# Descontos
impostoDeRenda = 0.11 * salarioBruto
inss = 0.08 * salarioBruto
sindicato = 0.05 * salarioBruto

# Calcula o salário líquido
salarioLiquido = salarioBruto - impostoDeRenda - inss - sindicato

print(f"\nSalário Bruto: R${salarioBruto:.2f}")
print(f"Desconto de Imposto de Renda (11%): R${impostoDeRenda:.2f}")
print(f"Desconto de INSS (8%): R${inss:.2f}")
print(f"Desconto de Sindicato (5%): R${sindicato:.2f}")
print(f"\nSalário Líquido: R${salarioLiquido:.2f}")
