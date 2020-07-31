from random import randint 
from time import sleep 
#Variaveis que guardará o números de vitórias do computador e do jogador, conforme forem sendo conquistadas.
ganhajogador = 0
ganhacomputador = 0
#Cabeçalho que haverá um registro para adicionar o nome que o jogador usará durante a partida.
print("=" * 60)
print("{:^60}".format("REGISTRO PARA O GAME"))
print("=" * 60)
nome= str(input("Nome do jogador: ")).title()
#Cabeçalho principal do jogo com as Regras.
print("=" * 60)
print("{:^60}".format("GAME: PEDRA, PAPEL E TESOURA"))
print("=" * 60)
sleep(2)
print('''REGRAS:
1 - Se escolher algum número que não está nas
opções o computador ganhará uma vitória

2 - Se escolher alguma letra o jogo será interropido''')
sleep(5)
#Começa a interação a partida do jogador contra o computador
while True:
    print(" ")
    print(f"[PLACAR: Jogador {nome} {ganhajogador} X {ganhacomputador} COMPUTADOR]")
    computador = randint(1,3)
    print(" ")
    jogador = int(input('''SUAS OPÇÕES:
    [1]PEDRA
    [2]PAPEL
    [3]TESOURA
    DIGITE: '''))
    print("Analisando...")
    sleep(3)
    if jogador == 1:
        print("{} escolheu Pedra".format(nome))
        if jogador == computador:
            print("Computador escolheu Pedra")
            sleep(2)
            print("Empate!!")
            print(" ")
        elif computador == 2:
            print("Computador escolheu Papel")
            sleep(2)
            print("Vencedor: Computador")
            print(" ")
            ganhacomputador += 1
        elif computador == 3:
            print("Computador escolheu Tesoura")
            sleep(2)
            print("Vencedor: {}".format(nome))
            print(" ")
            ganhajogador += 1
    elif jogador == 2:
        print("{} escolheu Papel".format(nome))
        if computador == 1:
            print("Computador escolheu Pedra")
            sleep(2)
            print("Vencedor: {}".format(nome))
            print(" ")
            ganhajogador += 1
        elif jogador == computador:
            print("Computador escolheu Papel")
            sleep(2)
            print("Empate!!")
            print(" ")
        elif computador == 3:
            print("Computador escolheu Tesoura")
            sleep(2)
            print("Vencedor: Computador")
            print(" ")
            ganhacomputador += 1
    elif jogador == 3:
        print("{} escolheu Tesoura".format(nome))
        if computador == 1:
            print("Computador escolheu Pedra")
            sleep(2)
            print("Vencedor: Computador")
            print(" ")
            ganhacomputador += 1
        elif computador == 2:
            print("Computador escolheu Papel")
            sleep(2)
            print("Vencedor: {}".format(nome))
            print(" ")
            ganhajogador += 1
        elif jogador == computador:
            print("Computador escolheu Tesoura")
            sleep(2)
            print("Empate!!")
            print(" ")
    else:
        ganhacomputador += 1 #Caso o jogador quebre a primeira regra
    if ganhajogador == 3 or ganhacomputador == 3:
        print(" ")
        print("[PLACAR FINAL: Jogador {} {} X {} COMPUTADOR]".format(nome, ganhajogador, ganhacomputador))
    if ganhajogador == 3:
        print(" ")
        print("RECEBA O CAMPEÃO!!!")
        for c in range(3,0,-1):
            sleep(c)
            print(c)
        print("O {} foi campeão com {} vitórias!!".format(nome,ganhajogador))
        break
    elif ganhacomputador == 3:
        print(" ")
        print('RECEBA O CAMPEÃO!!!')
        for c in range(3,0,-1):
            sleep(c)
            print(c)
        print("O Computador foi campeão com {} vitórias!!".format(ganhacomputador))
        break
print("Comecem os fogos!!!")
for c in range(0,10):
    print("BOOM!! BOOM!! POOWWWW!!!!")
    sleep(1)
print("Até a proxima!!")
sleep(5)
