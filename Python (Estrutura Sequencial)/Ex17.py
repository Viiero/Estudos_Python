#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

#Calcular a quantidade de tinta necessária
def calcular_tinta(area):
    cobertura_por_litro = 6
    folga_percentual = 0.1
    area_com_folga = area * (1 + folga_percentual)
    quantidade_litros = area_com_folga / cobertura_por_litro
    return quantidade_litros

#Calcular o custo da tinta em latas de 18 litros
def calcular_custo_latas(quantidade_litros):
    capacidade_lata = 18
    preco_lata = 80
    quantidade_latas = math.ceil(quantidade_litros / capacidade_lata)
    custo_total = quantidade_latas * preco_lata
    return quantidade_latas, custo_total

#Calcular o custo da tinta em galões de 3,6 litros
def calcular_custo_galoes(quantidade_litros):
    capacidade_galao = 3.6
    preco_galao = 25
    quantidade_galoes = math.ceil(quantidade_litros / capacidade_galao)
    custo_total = quantidade_galoes * preco_galao
    return quantidade_galoes, custo_total

#Calcular o custo da tinta misturando latas e galões
def calcular_custo_misturado(quantidade_litros):
    # Calcular a quantidade de latas necessárias
    quantidade_latas = math.floor(quantidade_litros / 18)
    # Calcular a quantidade restante em litros após usar latas
    restante_litros = quantidade_litros % 18
    # Calcular a quantidade de galões necessários para o restante
    quantidade_galoes = math.ceil(restante_litros / 3.6)
    
    # Calcular o custo total
    custo_total = quantidade_latas * 80 + quantidade_galoes * 25
    
    return quantidade_latas, quantidade_galoes, custo_total

#Função main
def main():
    # Solicitar ao usuário o tamanho da área a ser pintada
    area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

    # Calcular a quantidade de tinta necessária
    quantidade_litros = calcular_tinta(area_a_ser_pintada)

    # Calcular e exibe as opções de compra
    latas, custo_latas = calcular_custo_latas(quantidade_litros)
    galoes, custo_galoes = calcular_custo_galoes(quantidade_litros)
    latas_misturadas, galoes_misturados, custo_misturado = calcular_custo_misturado(quantidade_litros)

    print("\nQuantidade de tinta necessária: {:.2f} litros".format(quantidade_litros))
    print("\nOpções de compra:")
    print("1. Comprar apenas latas de 18 litros:")
    print("   Quantidade de latas: {}, Custo total: R$ {:.2f}".format(latas, custo_latas))
    print("2. Comprar apenas galões de 3,6 litros:")
    print("   Quantidade de galões: {}, Custo total: R$ {:.2f}".format(galoes, custo_galoes))
    print("3. Misturar latas e galões:")
    print("   Quantidade de latas: {}, Quantidade de galões: {}, Custo total: R$ {:.2f}".format(latas_misturadas, galoes_misturados, custo_misturado))

# Chama a função principal
if __name__ == "__main__":
    main()
