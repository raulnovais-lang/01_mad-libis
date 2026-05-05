import random
vidas=5
numero_aleatorio = random.randint(0,100)
while True:
    numero_escolhido = int (input("escolha um numero:"))

    if numero_escolhido==numero_aleatorio:
        print("você é dimais! Parabéns!!!")
        break
    else:
        if numero_escolhido > numero_aleatorio:
            print("o numero e menor entao vc perdeu")
        elif numero_escolhido < numero_aleatorio:
            print("o numero e maior então vc perdeu")
        vidas= vidas - 1

        if vidas==0:
            print("vc perdeu tudo, lindo! tchau obrigado! ")
            break
