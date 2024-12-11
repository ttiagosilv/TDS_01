def encontrar_maior_menor_media(numeros):
    maior = max(numeros)
    menor = min(numeros)
    media = sum(numeros) / len(numeros)
    return maior, menor, media

def main():
    numeros = []

    for i in range(5):
        numero = int(input("Digite o {}º número inteiro: ".format(i + 1)))
        numeros.append(numero)

    maior, menor, media = encontrar_maior_menor_media(numeros)

    print("O maior número lido é:", maior)
    print("O menor número lido é:", menor)
    print("A média aritmética dos números lidos é:", media)

if __name__ == "__main__":
    main()