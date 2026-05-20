def atributos_cartas():
    
    #Pedir ao jogador o nome, ataque e vida dos dois monstros, impede se ataque e vida forem menor ou igual a 0 ou se não for um número inteiro.
    monstro_1 = input("Digite o nome do primeiro monstro: ")

    try:
        ataque_1 = int(input("Digite o valor de ataque do primeiro monstro: "))
        hp_1 = int(input("Digite o valor da vida do primeiro monstro: "))

        if ataque_1 <= 0 or hp_1 <= 0:
            print("Ataque e vida devem ser números positivos.")
            return 
    
    except ValueError:
        print("Insira um número válido para ataque e vida.")
        return 

    monstro_2 = input("Digite o nome do segundo monstro: ")
    
    try:
        ataque_2 = int(input("Digite o valor de ataque do segundo monstro: "))
        hp_2 = int(input("Digite o valor da vida do segundo monstro: "))

        if ataque_2 <= 0 or hp_2 <= 0:
            print("Ataque e vida devem ser números positivos.")
            return 

    except ValueError:
        print("Insira um número válido para ataque e vida.")
        return 

    #Laço de repetição pro combate não parar até que um dos 2 monstros chegue a 0 ou menos de vida, o monstro 1 ataca, depois o 2 e assim até um perder. Exibe tbm o placar depois de cada ataque.
    while hp_1 > 0 and hp_2 > 0:
        hp_2 = atacar(monstro_1, ataque_1, monstro_2, hp_2)
        exibir_placar(monstro_1, hp_1, monstro_2, hp_2)

        if hp_2 > 0:
            hp_1 = atacar(monstro_2, ataque_2, monstro_1, hp_1)
            exibir_placar(monstro_1, hp_1, monstro_2, hp_2)

    #exibe o vencedor do combate
    if hp_1 > 0:
        print(f"{monstro_1} venceu")
    else:
        print(f"{monstro_2} venceu")


#função pra atacar, pega o nome do atacante, valor do ataque, nome defensor e vida, exibe quem atacou e quanto de dano, diminui na vida do defensor e exibe a vida restante
def atacar(nome_atacante, ataque, nome_defensor, hp_defensor):

    print(f"{nome_atacante} ataca {nome_defensor} causando {ataque} de dano.\n")
    hp_defensor -= ataque
    if hp_defensor < 0:
        hp_defensor = 0
    print(f"{nome_defensor} tem {hp_defensor} de HP restante.\n")

    return hp_defensor

#exibe o placar com nome e vida de cada monstro
def exibir_placar(nome1, hp1, nome2, hp2):
    if hp1 < 0:
        hp1 = 0
    if hp2 < 0:
        hp2 = 0
    print(f"Placar: {nome1} (HP: {hp1}) vs {nome2} (HP: {hp2})\n")


atributos_cartas()