import pandas as pd
import matplotlib.pyplot as plt
from helpers.generarTabla import crearTablaHTML
from data.generators.generarDatosConsumoEnergia import generarDatosConsumoEnergia


def construirDataFrameConsumoEnergia():
    # Traer los datos generados en el mock
    datosConsumoEnergia = generarDatosConsumoEnergia()

    # Construir el DataFrame
    consumoEnergiaDF = pd.DataFrame(datosConsumoEnergia, columns=['comuna', 'ttlpop', 'muestra', 'consumoEnergia', 'fecha', 'nombre', 'id'])

    # Imprimir el DataFrame para probar
    print(consumoEnergiaDF) 

    #Agrupando datos 
    datosAgrupados=consumoEnergiaDF.groupby("comuna")["id"].mean()
   
   #Graficando datos 
    plt.figure(figsize=(20,20))
    datosAgrupados.plot(kind='bar',color='green')
    plt.title('Consumo De Energia en Medellín')
    plt.xlabel('comuna')
    plt.ylabel('ID ')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig('./assets/img/ConsumoEnergia.png',format='png',dpi=600)
   #plt.show()
    
     
    #Probando...
    crearTablaHTML(consumoEnergiaDF,"ConsumoEnergia")

# Llamar a la función para construir el DataFrame de consumo de energía
construirDataFrameConsumoEnergia() 
