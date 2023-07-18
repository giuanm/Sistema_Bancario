import textwrap
def menu():
    menu = """\n
    ============= MENU ============
    [d]\tdepositar
    [p]\tpix
    [s]\tsacar
    [e]\textrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tsair
    => """
    return input(textwrap.dedent(menu))