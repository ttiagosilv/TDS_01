def quantidade_de_dinheiro(valor):
    quantidade = round(valor)
    return quantidade

def main():

    dinherio_total = float(input('Digite a quantidade de dinheiro:'))
    quantidade_total = quantidade_de_dinheiro(dinherio_total)
    print('A quantidade arredondada é', quantidade_total)

if __name__ =="__main__":
    main()