#Imagine uma brincadeira entre dois colegas, na qual um pensa um número e o outro deve fazer chutes até acertar o número imaginado.
#Como dica, a cada tentativa é dito se o número foi alto ou baixo. Neste contexto, elabore um algoritmo em python que leia o número imaginado e os chutes, mostrando ao final o número
#de tentativas necessárias para descobrir o número.

import random

def brincadeira_numero():
    # Gera um número aleatório de 1 a 100 para o colega tentar adivinhar
    numero_imaginado = random.randint(1, 100)
    
    tentativas = 0
    chute = 0
    
    print("Tente adivinhar o número imaginado entre 1 e 100!")
    
    while chute != numero_imaginado:
        try:
            chute = int(input("Digite seu chute: "))
            tentativas += 1

            if chute < numero_imaginado:
                print("Chute muito baixo. Tente novamente!")
            elif chute > numero_imaginado:
                print("Chute muito alto. Tente novamente!")
            else:
                print(f"Parabéns! Você acertou o número {numero_imaginado} em {tentativas} tentativas.")
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    brincadeira_numero()

