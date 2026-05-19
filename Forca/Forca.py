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
    resposta=input("escoha uma letra: ").upper()
    while len (resposta)!=1:
        resposta = input("eu disse apenas uma letra: ").upper()
        return resposta
# letra = perguntar_letra()
# print(letra)

def jogar_forca():
    #tela inicial de jogo
    print("""
********************************************************************
          *__*_______________________________________*_*
                     +_+___ Forca ____+_+
         *__*_______________________________________*_*
                +_+___ Acerte ou morra____+_+
         *__*_______________________________________*_*
         
********************************************************************
""")

    input ("aperte enter para apostar a sua vida")
    limpar()

    #chamar a função escolher_palavra e guardar em uma variavel 
    palavra_escolida = escolher_palavra()

    #chamar a forca para desenhar a forca 0
    desenhar_forca(0)

    #chamar a função gerar_palavra e guardar em uma variavel 
    lista_tracos = gerar_tracos(palavra_escolida)

    #imprimo a lista de traços 
    print("         ", *lista_tracos)

    #pergutar a letra e guardar em uma variavel 
    letra_chutada = perguntar_letra() 

    if letra_chutada not in palavra_escolida:

if __name__ == "__main__":
    jogar_forca()
