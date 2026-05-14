def calculadora_viagem():
    
    #Coleta os inputs
    destino_viagem = (input("Digite o destino da viagem: \n"))
    
    #Valida os inputs pra ver se são números e se sao positivos.
    try:
        orcamento_disponivel = float(input("Digite o orçamento disponível para a viagem: \n"))
        custo_passagem = float(input("Digite o custo estimado da passagem aérea: \n"))
        custo_diario = float(input("Digite o custo diário estimado para a viagem: \n"))
        duracao_viagem = int(input("Digite a duração da viagem em dias: \n"))
        
        if orcamento_disponivel < 0 or custo_passagem < 0 or custo_diario < 0 or duracao_viagem < 0:
            print("Por favor só numeros positivos")
            return
    
    except ValueError:
        print("Apenas números aqui, por favor!")
        return

    #Calcula os custos da viagem
    custo_diario_reais = custo_diario * 6.1
    custo_hospedagem = custo_diario_reais * duracao_viagem
    custo_total = custo_passagem + custo_hospedagem

    viavel = False
    dinheiro_falta = 0
    dinheiro_sobra = 0

    #Verifia se a viagem é viavel e calcula o dinheiro que vai sobrar ou faltar
    if custo_total <= orcamento_disponivel:
        if duracao_viagem > 0:
            viavel = True
            dinheiro_sobra = orcamento_disponivel - custo_total
        else:
            print("A duração da viagem deve ser maior que zero para ser viável.")
            return
    else:
        dinheiro_falta = custo_total - orcamento_disponivel

    #Printa o resumo da viagem detalhado
    print(f"\n---Resumo da viagem para {destino_viagem}---\n")
    print(f"Custo total da hospedagem: R${custo_hospedagem:.2f}\n")
    print(f"Custo total da viagem: R${custo_total:.2f}\n")
    if viavel:
        if dinheiro_sobra > 0:
            print(f"Orçamento possível para a viagem!! E ainda vai sobrar uma graninha!! R${dinheiro_sobra:.2f}\n")
        else:
            print("Orçamento possível para a viagem!! No limite, nem sobra nem falta\n")
        print("A viagem é viável!!\n")
    else:
        print(f"A viagem não é viável!! Falta uma grana infelizmente!! Falta exatamente R${dinheiro_falta:.2f} :(\n")

calculadora_viagem()
