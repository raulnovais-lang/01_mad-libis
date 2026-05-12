import os
import time
import random

dicionario_cores={"verde":20,
                  "azul":10,
                  "amarelo":60,
                  "lilas":"D0"}

lista_sequencia= []

def limpar_tela():
    os .system("color 02")
    os.system("cls")


def mudar_cor(cor):
    codigo_cor = dicionario_cores[cor]
    os.system(F"color {codigo_cor}")
    time.sleep(1)
    limpar_tela()
print("""

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
      *-*-*-*                GENIUS            *-*-*-*
      *-*-*-*          *-*-*-*-*-*-*-*-*-*     *-*-*-*
      *-*-*-*      REPITA AS CORES SEM ERRAR   *-*-*-*
      *-*-*-*                                  *-*-*-*
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
""")
input("pressoine enter para começar....")

limpar_tela()   
lista_cores = ["verde","azul","amarelo","lilas"]

while True:
    cor_aleatoria = random.choice(lista_cores)
    lista_sequencia.append(cor_aleatoria)

    for cor_lista in lista_sequencia:
        mudar_cor(cor_lista)

    print("""
        R=verde
        A=azul
        U=amarelo
        L=lilas""")
    resposta= input("digite a sequência correta: ")
    
    dicionario_abreviacoes=  {  "R":"verde",
                                "A":"azul",
                                "U":"amarelo",
                                "L":"lilas"}
    lista_de_respota= []

    for letra in resposta:
        cor = dicionario_abreviacoes.get(letra)
        lista_de_respota.append(cor)
    if lista_de_respota != lista_sequencia:
        print("vc errou linda")
        print("a sequencia era ")
        

