import pandas as pd

from data.generators.generadorcalidadaire import generarDatosCalidadAire
from helpers.generarTabla import crearTablaHTML

#1. PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATFRAME 

def contruirDataFrameCalidadAire():
    #Traigo los datos generados en el mock
    datosCalidadAire=generarDatosCalidadAire()

    #Constuyo el dataframe 
    calidadAireDF=pd.DataFrame(datosCalidadAire, columns=['comuna', 'ttlpop', 'muestra', 'ICA', 'fecha', 'nombre', 'id'])#columns=[] para agregar nombre de las columnas 

    #Linpiando el dataframe
    #1. Limpiando  (reemplazando valores)
    
    #calidadAireDF.replace('-',pd.NA,inplace=True)
    #calidadAireDF.replace('sin',pd.NA,inplace=True)

    #2.Limpiando (eliminando valores)
    calidadAireDF.replace('sin',pd.NA,inplace=True)
    calidadAireDF.dropna(inplace=True)

    #3.Filtrando datos para depurar la informacion 
    #FILTRAR DATOS ES OBTENER NUEVOS DATAFRAMES 
    #AL APLICAR CONDICIONES LOGICAS 

    #CONTAR DATOS 

    #CONSULTAR DATOS ESPECIFICOS 
    #filtroICAPositivo=calidadAireDF.query("(ICA>=20) and (ICA<50)")
    #filtroICAModerado=calidadAireDF.query("(ICA>=50) and (ICA<70)")
    filtroICAPeligroso=calidadAireDF.query("(ICA>=70)").value_counts()

    #print(filtroICAPositivo)
    #print("\n")
    #print(filtroICAModerado)
    print("\n")
    print(filtroICAPeligroso)
    #probando...
    
     
    #Probando...
    print(calidadAireDF)
    crearTablaHTML(calidadAireDF,"calidadAire")

contruirDataFrameCalidadAire()