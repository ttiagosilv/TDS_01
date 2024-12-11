def converter_segundos(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = (segundos % 3600) % 60
    return horas, minutos, segundos_restantes

segundos_evento = int(input("Digite o tempo de duração do evento em segundos: "))

horas, minutos, segundos = converter_segundos(segundos_evento)

print("Tempo do evento: {:02d}:{:02d}:{:02d}".format(horas, minutos, segundos))