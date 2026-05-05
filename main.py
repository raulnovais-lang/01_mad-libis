from j02.Adivinhaçao import jogar_adivinha_numero
from j01.madlibis import jogar_madlibis
from j03.par_ou_impar import jogar_par_impar
from j04.pedra_ import jogar_pedra_papel_tesoura
from j05.maior_menor import jogar_maior_menor

while 1==1:
    print(""" 
    ###########################################
    *       01- main libs                     *
    *       02- adinvinhação                  *
    *       03- par ou impar                  *
    *       04- pedra                         *
    *       05- maior ou menor                *
    *       0- sair                           *
    ###########################################
    """)
    escolha = int(input("por favor escolha o seu jogo:"))

    if escolha == 1:
        jogar_madlibis ()

    elif escolha == 2:
        jogar_adivinha_numero()

    elif escolha == 3:
        jogar_par_impar ()

    elif escolha == 4:
        jogar_pedra_papel_tesoura ()

    elif escolha == 5:
        jogar_maior_menor ()

    elif escolha == 0:
        print("foi otimo jogar com vc")
        break

