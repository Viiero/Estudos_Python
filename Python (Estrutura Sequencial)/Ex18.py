#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

import math

#Converter MB para Mbps
def converter_unidade(tamanho):
    novo_tamanho = tamanho * 8
    return novo_tamanho

#Calcular velocidade
def calcular_velocidade(velocidade, tamanho):
    velocidade_total = tamanho / velocidade
    return velocidade_total

def calcular_tempo(velocidade_total):
    tempo_aproximado = math.ceil(velocidade_total / 60)
    return tempo_aproximado

tamanho = float(input("Insira o tamanho do arquivo (em MB): "))

novo_tamanho = converter_unidade(tamanho)

velocidade = float(input("Insira a velocidade do link (em Mbps): "))

velocidade_final = calcular_velocidade(velocidade, novo_tamanho)

print("\nO tempo aproximado de download é de {} minutos. ".format(calcular_tempo(velocidade_final)))