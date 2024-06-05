import random

def generarDatosBiodiversidad():
    listaDatos = []
    
    for i in range(1000):  # Cantidad de datos creados
        # Generar datos aleatorios para cada atributo
        areaEstudio = random.choice(['Bosque Tropical', 'Sabana', 'Desierto', 'Zona Costera', 'Montaña', 'Humedal'])
        planificacionMuestreo = random.choice(['Estacional', 'Anual', 'Mensual', 'Quincenal'])
        recopilacionDatos = random.choice(['Observación Directa', 'Fototrampeo', 'Captura y Liberación', 'Análisis de Huellas'])
        identificacionEspecies = random.choice(['Flora', 'Fauna', 'Microorganismos', 'Insectos', 'Aves', 'Mamíferos'])
        id = random.randint(0, 1000000)
        
        # Crear una lista con los datos generados
        datosBiodiversidad = [areaEstudio, planificacionMuestreo, recopilacionDatos, identificacionEspecies, id]
        
        # Agregar los datos generados a la lista principal
        listaDatos.append(datosBiodiversidad)
    
    return listaDatos

# Imprimir los datos generados
print(generarDatosBiodiversidad())
