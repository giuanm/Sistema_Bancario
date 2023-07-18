from menu import menu
from deposito import depositar
from debito import debitar
from criar_usuario import criar_usuario
from criar_conta import criar_conta
from listar_contas import listar_contas

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

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

        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()