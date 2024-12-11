def codigo_do_caractere(numero):
    reultado_da_quantidade = ord(numero)
    return reultado_da_quantidade

caractere = input('Digite um caractere qualquer:')
resultado = codigo_do_caractere(caractere)
print('O código do carctere é', resultado)
