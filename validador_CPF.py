import sys
import re
def validador(cpf):
    eh_sequencia = cpf == cpf[0]*len(cpf)

    if eh_sequencia:
        print("Daos inválidos, o CPF enviado foi um sequencia.")
        sys.exit()

    x = re.sub(
        r'[^0-9]',
        '',
        cpf
    )

    soma = 0
    dig1 = 0
    dig2 = 0
    listas = []

    for s in x:
        listas += s
    d1 = listas.pop()
    d2 = listas.pop()
    v = d1+d2

    indic = len(listas)

    for i in listas:
        soma += int(i)*(indic+1)
        indic -= 1

    dig1 = (soma*10)%11
    dig1 = dig1 if dig1 <= 9 else 0

    listas.append(dig1)
    indic = len(listas)
    soma = 0

    for i in listas:
        soma += int(i)*(indic+1)
        indic -= 1
    dig2 = (soma*10)%11
    dig2 = dig2 if dig2 <= 9 else 0
    listas.append(dig2)

    v2 = str(dig1) + str(dig2)

    if v == v2:
        r = True
    else:
        r = False
    
    return r