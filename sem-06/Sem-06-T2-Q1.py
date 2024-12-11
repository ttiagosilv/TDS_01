def contar_caracteres_sem_espacos(frase):
    frase_sem_espacos = frase.strip()
    num_caracteres = len(frase_sem_espacos)
    return num_caracteres

def main():
    frase = input("Digite uma frase: ")
    num_caracteres = contar_caracteres_sem_espacos(frase)
    print("O número de caracteres na frase (sem espaços em branco no início ou no final) é:", num_caracteres)

if __name__ == "__main__":
    main()