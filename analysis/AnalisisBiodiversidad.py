import pandas as pd

# Asegúrate de tener el módulo generadorBiodiversidad en el path correcto
from data.generators.generadorBiodiversidad import generarDatosBiodiversidad
from helpers.generarTabla import crearTablaHTML

# Función para construir el DataFrame de biodiversidad
def construirDataFrameBiodiversidad():
    # Traigo los datos generados en el mock
    datosBiodiversidad = generarDatosBiodiversidad()

    # Construyo el DataFrame
    biodiversidadDF = pd.DataFrame(datosBiodiversidad, columns=['areaEstudio', 'planificacionMuestreo', 'recopilacionDatos', 'identificacionEspecies', 'id']) # columns=[] para agregar nombre de las columnas

    # Probando...
    print(biodiversidadDF)
    crearTablaHTML(biodiversidadDF, "biodiversidad")

construirDataFrameBiodiversidad()
