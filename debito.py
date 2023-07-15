def debitar(LIMITE_SAQUES, limite, saldo, extrato, numero_saques, opcao):
    valor = float(input("Informe o valor: "))

    if opcao == "s":

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")
        
        elif excedeu_saques:
            print("Operações falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    else:
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Pix: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques