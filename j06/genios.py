import os
import time



def limpar_tela():
    os .system("color 42")
    os.system("cls")


def mudar_cor(cor):
    os.system(F"color{cor}")
    time.sleep(1)
    limpar_tela()

mudar_cor(80)
mudar_cor(70)
mudar_cor(30)
mudar_cor(10)