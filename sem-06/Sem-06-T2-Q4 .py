def anos_espacias(idade_terrestre):
    conversao = int(idade_terrestre * 0.5)
    return conversao

def main ():
    idade_terrestre = float(input('Digite a quantida de de anos terrestres:'))
    idade_total = anos_espacias(idade_terrestre)
    print("A idade em anos espaciais é:", idade_total)

if __name__ == "__main__":
    main()