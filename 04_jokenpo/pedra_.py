import random
print("""
*****************************************************************************************
***                                Pedra                                              ***
***                                Papel                                              ***
***                                Tesoura                                            ***
*****************************************************************************************

""")
escolha= input("escolha um Pedra,papel,tesoura: ")
escolha_computador = random.choice(["pedra","papel","tesoura"])
print(f"o que eu escolhi foi {escolha_computador}")
if escolha== escolha_computador:
    print("deu o empate")
elif escolha=="pedra" and escolha_computador=="tesoura":
    print("vc ganhou")
elif escolha == "papel" and escolha_computador== "pedra":
    print("vc ganhou...")
elif escolha == "tesoura" and escolha_computador== "papel":
    print("vc ganhou...")
else:
    print("vc perdeu")