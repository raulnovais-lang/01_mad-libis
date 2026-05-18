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
def desenhar_forca (erro):
    """imprima o desenho da forca denperdendo de quantidade de erros"""
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