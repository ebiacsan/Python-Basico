import random

def jogar():
    print("######################################")
    print("## Bem vindo ao Jogo da Adivinhação ##")
    print("######################################\n")

    #numero_secreto = random.seed(1000)
    numero_secreto = random.randrange(1, 1001) #gera número entre 1 e 1000
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print(" [1] - Fácil \n [2] - Médio \n [3] - Difícil\n")
    nivel = int(input("Escolha o nível: "))

    if(nivel == 1):
        print("Nível fácil\n")
        total_de_tentativas = 10
    elif(nivel == 2):
        print("Nível médio\n")
        total_de_tentativas = 5
    else:
        print("Nível difícil\n")
        total_de_tentativas = 3

    tentativa_restante = 1
    while(tentativa_restante <= total_de_tentativas):
        print("Tentativa: {} de {}". format(tentativa_restante, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 1000: "))
        #print("Você digitou", chute)

        if((chute < 1) or (chute > 1000)):
            print("Você deve digitar um número entre 1 e 1000")
            continue
            tentativa_restante -= 1

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        pontos_perdidos = numero_secreto - chute

        if(acertou):
            print("Você acertou o número secreto, meu parceiro!!")
            break
        else:
            if(chute_maior):
                print("Opa! Seu chute foi maior que o número secreto!")
            else:
                print("Seu palpite foi menor que o número secreto! ")
            pontos -= abs(pontos_perdidos)

        tentativa_restante += 1

    print("\nO número era: {}".format(numero_secreto))
    print("FIM DO JOGO!!\n")

if(__name__== "__main__"):
    jogar()