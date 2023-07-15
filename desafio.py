from deposito import depositar
from debito import debitar
menu = """

[d] depositar
[p] pix
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = depositar()
        saldo = deposito[0]
        extrato = deposito[1]
    
    elif opcao == "s":
        saque = debitar(LIMITE_SAQUES, limite, saldo, extrato, numero_saques, opcao)
        saldo = saque[0]
        extrato = saque[1]
        numero_saques = saque[2]
    
    elif opcao == "p":
        input("Informe a chave pix de destino: ")
        transf = debitar(LIMITE_SAQUES, limite, saldo, extrato, numero_saques, opcao)
        extrato = transf[1]
        print("")
        saldo = transf[0]
    
    elif opcao == "e":
        print("\n************* EXTRATO ************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("**********************************")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
