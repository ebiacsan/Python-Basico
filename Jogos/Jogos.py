import Adivinhacao
import Forca
 
def escolhe_jogo():
    print("#####################################")
    print("######## Escolha o seu Jogo! ########")
    print("#####################################\n")

    print(" [1] - Adivinhação \n [2] - Forca")

    jogo = int(input(" Qual jogo? "))
    print("\n")

    if(jogo == 1):
        print("Jogando Adivinhação\n")
        Adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogando Forca\n")
        Forca.jogar()

if(__name__== "__main__"):
    escolhe_jogo()