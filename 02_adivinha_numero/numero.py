import random
print(""" 
  ___      _ _       _       _                                                         
 / _ \    | (_)     (_)     | |                                                        
/ /_\ \ __| |___   ___ _ __ | |__   ___    ___    _ __  _   _ _ __ ___   ___ _ __ ___  
|  _  |/ _` | \ \ / / | '_ \| '_ \ / _ \  / _ \  | '_ \| | | | '_ ` _ \ / _ \ '__/ _ \ 
| | | | (_| | |\ V /| | | | | | | |  __/ | (_) | | | | | |_| | | | | | |  __/ | | (_) |
\_| |_/\__,_|_| \_/ |_|_| |_|_| |_|\___|  \___/  |_| |_|\__,_|_| |_| |_|\___|_|  \___/ 
                                                                                       
                                                                                       """)


print("""
*****************************************************************************************
***                                                                                   ***
***                            1- noob (de 1 á 10)                                    ***
***                            2- médio (de 1 á 20)                                   ***
***                            3- Profissional (de 1 á 50)                            ***
***                            4- SENAI (De 1 à 200)                                  ***
*****************************************************************************************

""")
nivel=int(input("escolha um nivel: "))


if nivel==1:
    numero_aleatorio = random.randint(1,10)

    numero=int(input ("adivinhe o numero: "))

    if numero_aleatorio==numero:
        print("você acertou")
    else:
        print(f"vc errou o numero que ele penssou foi {numero_aleatorio}")


if nivel==2:
    numero_aleatorio = random.randint(1,20)

    numero=int(input ("adivinhe o numero: "))

    if numero_aleatorio==numero:
        print("você acertou")
    else:
        print(f"vc errou o numero que ele penssou foi {numero_aleatorio}")

if nivel==3:
    numero_aleatorio = random.randint(1,50)

    numero=int(input ("adivinhe o numero: "))

    if numero_aleatorio==numero:
        print("você acertou")
    else:
        print(f"vc errou o numero que ele penssou foi {numero_aleatorio}")
        

if nivel==4:
    numero_aleatorio = random.randint(1,200)

    numero=int(input ("adivinhe o numero: "))

    if numero_aleatorio==numero:
        print("você acertou")
    else:
        print(f"vc errou o numero que ele penssou foi {numero_aleatorio}")




