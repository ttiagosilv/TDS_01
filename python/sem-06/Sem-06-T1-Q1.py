def contar_de_caractere(nome):
    quantidade_de_caractere = len(nome)
    return quantidade_de_caractere

nome = input('Digite um nome qualquer:')
resultado = contar_de_caractere(nome)
print(f'O nome possui', resultado, 'caracteres')

