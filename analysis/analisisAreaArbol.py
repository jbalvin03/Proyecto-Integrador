import pandas as pd
import random
import matplotlib.pyplot as plt

from data.generators.generadorcalidadaire import generarDatosCalidadAire
from helpers.generarTabla import crearTablaHTML

# Función para generar datos de área de árboles
def generarAreaArboles():
    listaDatos = []
    for i in range(1000):
        corregimiento = random.choice(['Cacerí', 'Cuturu', 'El Pando', 'La Ilusion', 'Margento', 'Palanca', 'Palomar', 'Puerto Colombia'])
        nombreArbol = random.choice(['Encina', 'Alcornoque', 'Acebuche', 'Olivo Silvestre', 'Ipuana', 'Acacia Mimosa', 'Limonero', 'Pino'])
        idArbol = random.randint(1, 100)
        hectariasSembradas = random.choice(['500', '1000', '2000', '2500', '3000'])
        frutaArbol = random.choice(['Fresa', 'Mango', 'Manzana', 'Aguacate'])
        areaArbol = [corregimiento, nombreArbol, idArbol, hectariasSembradas, frutaArbol]
        
        listaDatos.append(areaArbol)
    
    return listaDatos

# Para analizar datos con Python, debemos construir un DATAFRAME
def construirDataFrameAreaArboles():
    # Traigo los datos generados
    datosAreaArboles = generarAreaArboles()

    # Construyo el DataFrame
    areaArbolesDF = pd.DataFrame(datosAreaArboles, columns=['corregimiento', 'nombreArbol', 'idArbol', 'hectariasSembradas', 'frutaArbol'])

    # Probando...
    #print(areaArbolesDF)

    #Agrupando datos 
    datosAgrupados=areaArbolesDF.groupby("corregimiento")["idArbol"].mean()
   
   #Graficando datos 
    plt.figure(figsize=(20,20))
    datosAgrupados.plot(kind='bar',color='green')
    plt.title('Hectarias de arboles sembrados en Medellín')
    plt.xlabel('corregimiento')
    plt.ylabel('IDA (ID Arbol)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig('./assets/img/areaArboles.png',format='png',dpi=600)
   #plt.show()
    
     
    #Probando...
    #crearTablaHTML(areaArbolesDF,"areArboles")

#Llamando a la función para construir el DataFrame y mostrar los datos
construirDataFrameAreaArboles()