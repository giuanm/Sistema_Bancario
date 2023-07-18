from validador_CPF import validador
from filtrar_usuario import filtrar_usuario

def criar_usuario(usuarios):
    cpf = input("Informe o CPF(somente números): ")
    if validador(cpf):
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
            print("\n@@@ Jáexiste usuário com esse CPF! @@@")
            return
        
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, núm - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("==== Usuário cadastrado com sucesso! ====")
    else:
        print(f"\n@@@ CPF inválido!!! @@@")