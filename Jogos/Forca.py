import random

def jogar():
    # Boas vindas
    boas_vindas()

    # Abre arquivo:
    palavra_secreta = manipulando_arquivo()

    # Adiciona _ para cada letra da palavra escolhida:
    letras_certas = list_comprehesion(palavra_secreta)

    erros = 0
    acertou = False    #Ele está errando
    enforcou = False  #Ainda tem chances de acertar
    
    print(letras_certas)
    # Pede o chute so player:
    while(not enforcou and not acertou):
        chute = qual_chute()

        # Procura letras na palavra secreta:
        if(chute in palavra_secreta):
            marca_letras_na_posicao(chute, letras_certas, palavra_secreta)

        # Contabiliza os erros:
        else:
            erros += 1
            print("Ops! Você errou! Faltam {} tentativas" .format(5-erros))
            desenha_forca()

        enforcou = erros == 5
        acertou = "_" not in letras_certas
        print(letras_certas)
    # Mensagem final de ganho ou perda:
    if acertou:
        you_WIN()
    else:
        you_LOSE()

    mensagem_final()


def boas_vindas():
        print("####################################")
        print("#### Bem vindo ao Jogo da Forca ####")
        print("####################################\n")


def manipulando_arquivo():
    # with open("frutas.txt") as arquivo:
    #     for line in arquivo:
    #         print(line)
    arquivo = open("frutas.txt", "r")
    frutinhas = []
    # Tira a quebra de linha e espaços com strip():
    for line in arquivo:
        line = line.strip()
        frutinhas.append(line)

    arquivo.close()
    # Escolhe aleatoriamente a palavra:
    numero = random.randrange(0, len(frutinhas))
    palavra_secreta = frutinhas[numero].upper()
    return palavra_secreta


def list_comprehesion(palavra):
    #for i in range(0, len(palavra_secreta)): #Modo que fiz no desafio Oi
    #   letras_certas.append("_")
    return ["_" for letra in palavra]


def qual_chute():
    chute = str(input("Qual letra? "))
    chute = chute.strip().upper()
    return chute


def marca_letras_na_posicao(chute, letras_certas, palavra_secreta): #sempre devo lembrar de passar os parametros 
    posicao = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_certas[posicao] = letra
        posicao += 1


def desenha_forca():
    pass


def you_WIN():
    print("\nVOCÊ GANHOU!!")
    #COLOCAR ASCII ARTE DE VENCEDOR

def you_LOSE():
    print("\nPoxa! Você PERDEU!")
    # COLOCAR ASCII ARTE DE PERDEDOR


def mensagem_final():
    print("\n\nFIM DO JOGO!!\n")

if(__name__== "__main__"):
    jogar()