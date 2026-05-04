import random
def jogar_adivinha_numero():
   numero_aleatorio = random.randint(0,20)

   numero_escolhido = int (input("escolha um numero:"))

   if numero_escolhido==numero_aleatorio:
      print("você é dimais! Parabéns!!!")
   else:
      print("vc é fraco")
      print (f"o numero era : {numero_aleatorio}") 