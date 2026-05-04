import random

def jogar_par_impar ():

    print("""
    *****************************************************************************************
    ***                                                                                   ***
    ***                                par ou impar                                       ***
    ***                                                                                   ***
    *****************************************************************************************

    """)
    escolha= input("digite o par ou impar: ")

    if escolha=="par":
        print("eu sou impar")

    else:
        print("eu sou par")

    numero= int(input("escolha um numero(0,10)"))
    numero_aleatorio=random.randint(0,10)

    print(f"o numero que eu escolhi foi {numero_aleatorio}")

    soma=numero+numero_aleatorio
    resto=numero%2

    if resto==0 and escolha=="par":
        print("vc ganhou!")
    elif resto==1 and escolha== "impar":
        print("vc ganhou")
    else:
        print("vc perdeu")