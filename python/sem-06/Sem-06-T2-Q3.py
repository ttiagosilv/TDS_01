def calcular_total(preco_macas, preco_bananas):
    valor = (3 * preco_macas) + (2 * preco_bananas)
    return valor

def main():

    preco_macas = float(input('Digite o valor de uma maçã:'))
    preco_bananas = float(input('Digite o valor de uma banana:'))
    valor_total = calcular_total(preco_macas,preco_bananas)

    total_formatado = "{:.2f}".format(valor_total)

    print("O valor total das frutas é de:", total_formatado)

if __name__ == "__main__":
    main()