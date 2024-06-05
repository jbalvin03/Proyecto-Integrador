#RUTINA PARA GENERAR DE FORMA ALEATORIA MULTIPLES DATOS CON PYTHON

import random

def generarDatosCalidadAire():
    listaDatos=[]
    for i in range(1000):#Cantidad de datos creados 
        comuna=random.choice(['comuna 1 popular', 'comuna 2 santa cruz','comuna 3 marrique','comuna 4 aranjuez','comuna 5 castilla', 'comuna 6 12 octubre','comuna 7 robledo', 'comuna 8 villa hermosa', 'comuna 9 buenos aires','comuna 10 la candelaria', 'comuna 11 laureles-estadio ', 'comuna 12 la america',  'comuna 13 san javier', 'comuna 14 el poblado', 'comuna 15 guayabal','-','sin', 'comuna 16 belen'])
        totalPoblacion=random.choice(['300', '4500', '5000', '10000'])
        tamanoMuestra=random.choice(['1000', '2000', '3500', '6000'])
        ica=random.randint(20,100)#randint es para generar numero aleatorio 
        fecha=random.choice(['2024-05-14", "2024-05-15'])
        nombreEncuestado=random.choice(['pedro paramo', 'sandra mor', 'martina la peligrosa', 'kevin albeiro', 'valentina mor', 'juan jimeno'])
        id=random.randint(0,1000000)
        calidadAire=[comuna,totalPoblacion,tamanoMuestra,ica,fecha,nombreEncuestado,id]

        listaDatos.append(calidadAire)

    return listaDatos
print(generarDatosCalidadAire())