#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

#Calcular a quantidade de latas necessárias
def calcular_latas(area):
    cobertura_por_lata = 18 * 3
    quantidade_latas = math.ceil(area / cobertura_por_lata)
    return quantidade_latas

#Calcular o preço total
def calcular_preco(quantidade_latas):
    preco_por_lata = 80.00
    preco_total = quantidade_latas * preco_por_lata
    return preco_total

#Entrada
try:
    tamanho_area = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))
    
    # Verificar se o tamanho da área é válido
    if tamanho_area <= 0:
        print("Por favor, insira um valor válido para o tamanho da área.")
    else:
        # Calcular a quantidade de latas e o preço total
        latas_necessarias = calcular_latas(tamanho_area)
        preco_total = calcular_preco(latas_necessarias)

        # Exibir os resultados
        print("\nQuantidade de latas necessárias: {}".format(latas_necessarias))
        print("Preço total: R$ {:.2f}".format(preco_total))

except ValueError:
    print("Por favor, insira um valor numérico para o tamanho da área.")
