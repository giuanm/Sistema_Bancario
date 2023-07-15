
def depositar():
    valor = float(input("Informe o valor do depósito: "))

    saldo = 0
    extrato = ""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato