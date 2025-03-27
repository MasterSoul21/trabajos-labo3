primera_hora = int(input("Por favor, ingrse la primera hora: "))
primer_minuto = int(input("Por favor, ingrese los minutos (primera hora): "))
segunda_hora = int(input("Por favor, la segunda hora: "))
segundo_minutos = int(input("Por favor, ingrese los minutos(segunda hora): "))

if primera_hora < 24 and segunda_hora < 24:
    if primera_hora > segunda_hora:
        total_hora = primera_hora - segunda_hora
    else:
        total_hora = segunda_hora - primera_hora

if primer_minuto < 60 and segundo_minutos < 60:
    if primer_minuto > segundo_minutos:
        total_minutos = primer_minuto - segundo_minutos
    else:
        total_minutos = segundo_minutos - primer_minuto

print(f"{total_hora} horas y {total_minutos} minutos")