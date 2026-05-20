def atributos_cartas():
    
    monstro_1 = input("Digite o nome do primeiro monstro: ")

    try:
        ataque_1 = int(input("Digite o valor de ataque do primeiro monstro: "))
        vida_1 = int(input("Digite o valor da vida do primeiro monstro: "))

        if ataque_1 < 0 or vida_1 < 0:
            print("Ataque e vida devem ser números positivos.")
            return 
    
    except ValueError:
        print("Insira um número válido para ataque e vida.")
        return 

    monstro_2 = input("Digite o nome do segundo monstro: ")
    
    try:
        ataque_2 = int(input("Digite o valor de ataque do segundo monstro: "))
        vida_2 = int(input("Digite o valor da vida do segundo monstro: "))

        if ataque_2 < 0 or vida_2 < 0:
            print("Ataque e vida devem ser números positivos.")
            return 

    except ValueError:
        print("Insira um número válido para ataque e vida.")
        return
    

    atacar(monstro_1, ataque_1, monstro_2, vida_2)

def atacar(nome_atacante, ataque, nome_defensor, hp_defensor):

    print(f"{nome_atacante} ataca {nome_defensor} causando {ataque} de dano.")
    hp_defensor -= ataque
    print(f"{nome_defensor} tem {hp_defensor} de HP restante.")

def exibir_placar(nome1, hp1, nome2, hp2):
    print(f"Placar: {nome1} (HP: {hp1}) vs {nome2} (HP: {hp2})")


atributos_cartas()