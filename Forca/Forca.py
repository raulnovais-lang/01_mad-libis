import os
import random

def limpar(): 
    """função para limpar a tela""" 
    os.system("cls")

def escolher_palavra() -> str:
    """escolhe e retorna uma palavra aleatória """
    palavras = ["CASA", 
                "CELULAR",
                "PORTA", 
                "DANIELE",
                "COXINHA"]
    palavra_aleatoria = random.choice(palavras)
    return palavra_aleatoria 

#palavra_escolida = escolher_palavra()

#print(palavra_escolida)
def desenhar_forca (erro:int):
    """imprima o desenho da forca denperdendo de quantidade de erros"""
    limpar()
    if erro == 0:
        print(r"""
         _____          
        |     
        |    
        |      
        |
        |
        |       """)

    elif erro == 1:
        print(r"""
         _____
        |     |         
        |    ( )
        |    
        |      
        |
        |
        |       """)

    elif erro == 2:
        print(r"""
         _____          
        |    ( )
        |     |
        |      
        |
        |
        |       """)
    elif erro == 3:
        print(r"""
         _____          
        |    ( )
        |     |
        |   / |
        |
        |
        |       """)


    elif erro == 4:
        print(r"""
         _____          
        |    ( )
        |     |
        |   / | \
        |
        |
        |       """)
    elif erro == 5:
        print(r"""
         _____          
        |    ( )
        |     |
        |   / | \
        |     |
        |   /
        |       """)

    elif erro == 6:
        print(r"""
         _____          
        |    ( )
        |     |
        |    /|\
        |     |
        |    / \
        |       """)

#desenhar_forca(5) - somente para testar se está correto

def gerar_tracos(palavra: str) -> list:
    """gere e retorna uma lista conteudos underlines (_) na mesma quantidade que as letras da palavra"""
    quantidade_de_letras =len(palavra)
    tracos = []    
#usando while e o contador 
    contador = 0
    while contador < quantidade_de_letras:
        tracos.append("_")
        contador = contador + 1
    
    #while len (tracos) < quantidade_de_letras
    #tracos.append("_")
    
    #for x in palavra:
    #    tracos.append("_")
    return tracos

def perguntar_letra() -> str:
    resposta=input("escoha uma palvra: ").upper()
    while len (resposta)!=1:
        resposta = input("eu disse apenas uma letra: ").upper()
        return resposta
letra = perguntar_letra()
print(letra)

def jogar_forca():
    #tela inicial de jogo
    pass
