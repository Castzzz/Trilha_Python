def calculadora_viagem():
    
    destino_viagem = (input("Digite o destino da viagem: "))
    orcamento_disponivel = float(input("Digite o orçamento disponível para a viagem: "))
    custo_passagem = float(input("Digite o custo estimado da passagem aérea: "))
    custo_diario = float(input("Digite o custo diário estimado para a viagem: "))
    duracao_viagem = int(input("Digite a duração da viagem em dias: "))

    custo_diario_reais = custo_diario * 6.1
    custo_hospedagem = custo_diario_reais * duracao_viagem
    custo_total = custo_passagem + custo_hospedagem

    viavel = False

    if custo_total <= orcamento_disponivel:
        print("Orçamento possível!!!\n")
        if duracao_viagem > 0:
            viavel = True
            dinheiro_sobra = orcamento_disponivel - custo_total
            if dinheiro_sobra > 0:
                print(f"Ainda vai sobrar R${dinheiro_sobra:.2f} pra fazer umas comprinhas!!!")
            else:
                print("O orçamento perfeito! No limite, nem sobra nem falta")
    else:
        print("Orçamento não possível!!!")
        dinheiro_falta = custo_total - orcamento_disponivel
        print(f"Faltam R${dinheiro_falta:.2f} para conseguir viajar\n")


calculadora_viagem()
