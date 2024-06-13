import pandas as pd
import matplotlib.pyplot as plt

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
    #filtroICAPeligroso=calidadAireDF.query("(ICA>=70)").value_counts()

    #print(filtroICAPositivo)
    #print("\n")
    #print(filtroICAModerado)
    print("\n")
    
    #Agrupando datos 
    datosAgrupados=calidadAireDF.groupby("comuna")["ICA"].mean()
   
   #Graficando datos 
    plt.figure(figsize=(20,20))
    datosAgrupados.plot(kind='bar',color='green')
    plt.title('Calidad de aire por comuna en Medellin')
    plt.xlabel('comuna')
    plt.ylabel('ICA (Indice Calidad Aire)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig('./assets/img/calidadAire.png',format='png',dpi=600)
   #plt.show()
    
     
    #Probando...
    #crearTablaHTML(calidadAireDF,"calidadAire")

contruirDataFrameCalidadAire()
