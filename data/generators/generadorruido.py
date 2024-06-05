import random

def generarDatosRuido():
    listaDatos = []
    for i in range(1000):
        comuna = random.choice([
            'comuna 1 popular', 'comuna 2 santa cruz', 'comuna 3 manrique', 'comuna 4 aranjuez', 
            'comuna 5 castilla', 'comuna 6 12 de octubre', 'comuna 7 robledo', 'comuna 8 villa hermosa', 
            'comuna 9 buenos aires', 'comuna 10 la candelaria', 'comuna 11 laureles-estadio', 
            'comuna 12 la america', 'comuna 13 san javier', 'comuna 14 el poblado', 
            'comuna 15 guayabal', 'comuna 16 belen'
        ])
        totalPoblacion = random.choice(['300', '4500', '5000', '10000'])
        tamanoMuestra = random.choice(['1000', '2000', '3500', '6000'])
        decibelesNoche = random.uniform(30.0, 80.0)  # decibeles de ruido en la noche
        decibelesDia = random.uniform(40.0, 90.0)    # decibeles de ruido en el día
        fechaEncuesta = random.choice(['2024-05-14', '2024-05-15'])
        nombre = random.choice([
            'pedro paramo', 'sandra mor', 'martina la peligrosa', 'kevin albeiro', 
            'valentina mor', 'juan jimeno'
        ])
        id = random.randint(0, 1000000)
        nombreEdificio = random.choice([
            'Edificio Central', 'Torre Sur', 'Condominio Norte', 'Residencias El Sol', 
            'Centro Empresarial', 'Edificio Las Palmas'
        ])
        
        ruido = [
            comuna, totalPoblacion, tamanoMuestra, decibelesNoche, 
            decibelesDia, fechaEncuesta, nombre, id, nombreEdificio
        ]
        
        listaDatos.append(ruido)
    
    return listaDatos


