import pandas as pd
import matplotlib.pyplot as plt

# Asegúrate de tener el módulo generadorBiodiversidad en el path correcto
from data.generators.generadorBiodiversidad import generarDatosBiodiversidad
from helpers.generarTabla import crearTablaHTML

# Función para construir el DataFrame de biodiversidad
def construirDataFrameBiodiversidad():
    # Traigo los datos generados en el mock
    datosBiodiversidad = generarDatosBiodiversidad()

    # Construyo el DataFrame
    biodiversidadDF = pd.DataFrame(datosBiodiversidad, columns=['areaEstudio', 'planificacionMuestreo', 'recopilacionDatos', 'identificacionEspecies', 'id']) # columns=[] para agregar nombre de las columnas

    #Agrupando datos 
    datosAgrupados=biodiversidadDF.groupby("areaEstudio")["id"].mean()
   
   #Graficando datos 
    plt.figure(figsize=(20,20))
    datosAgrupados.plot(kind='bar',color='green')
    plt.title('Calidad de ruido por comuna en Medellin')
    plt.xlabel('areaEstudio')
    plt.ylabel('ID ')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig('./assets/img/Biodiversidad.png',format='png',dpi=600)
   #plt.show()


    # Probando...
    #print(biodiversidadDF)
    #crearTablaHTML(biodiversidadDF, "biodiversidad")

construirDataFrameBiodiversidad()
