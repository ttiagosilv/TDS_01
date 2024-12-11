def conversao_de_temperatura(celsius):
    fahrenheit = (celsius * 9 / 5)+ 32
    return fahrenheit

def main():
    celsius = float(input('Digite a temperatura em graus celsius:'))
    fahrenheit = conversao_de_temperatura(celsius)
    print('A temperatura em fahrenheit é:', fahrenheit)

if __name__ == "__main__":
    main()