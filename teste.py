def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor

    desconto = str(input())
 
    if desconto == "20%":
        print(f'Valor total: {0.8*total:.2f}')
    
    else:
        print(f'Valor total: {0.8*total:.2f}')
main()