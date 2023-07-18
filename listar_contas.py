import textwrap

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']["nome"]}
        """
        print("=" *50)
        print(textwrap.dedent(linha))