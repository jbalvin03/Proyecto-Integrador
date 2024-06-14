import random

def generarDatosConsumoEnergia():
    listaDatos = []
    for _ in range(1000):  # Generar 1000 conjuntos de datos de consumo de energía
        comuna = random.choice([
            'Comuna 1 Popular', 'Comuna 2 Santa Cruz', 'Comuna 3 Manrique', 'Comuna 4 Aranjuez', 
            'Comuna 5 Castilla', 'Comuna 6 12 de Octubre', 'Comuna 7 Robledo', 'Comuna 8 Villa Hermosa', 
            'Comuna 9 Buenos Aires', 'Comuna 10 La Candelaria', 'Comuna 11 Laureles-Estadio', 
            'Comuna 12 La América', 'Comuna 13 San Javier', 'Comuna 14 El Poblado', 
            'Comuna 15 Guayabal', 'Comuna 16 Belén'
        ])
        totalPoblacion = random.randint(300, 10000)  # Población total (número entero)
        tamanoMuestra = random.randint(1000, 6000)    # Tamaño de muestra (número entero)
        consumoEnergia = random.uniform(100.0, 1000.0)  # Consumo de energía en kWh
        fechaRegistro = random.choice(['2024-05-14', '2024-05-15'])  # Fecha de registro
        nombreCliente = random.choice([
            'Cliente 1', 'Cliente 2', 'Cliente 3', 'Cliente 4', 'Cliente 5'
        ])  # Nombre del cliente
        identificador = random.randint(0, 1000000)  # Identificador único

        datosEnergia = [
            comuna, totalPoblacion, tamanoMuestra, consumoEnergia, 
            fechaRegistro, nombreCliente, identificador
        ]

        listaDatos.append(datosEnergia)

    return listaDatos

datos_consumo_energia = generarDatosConsumoEnergia()