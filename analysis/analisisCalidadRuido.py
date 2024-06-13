import pandas as pd 
import matplotlib.pyplot as plt

from data.generators.generadorruido import generarDatosRuido
from helpers.generarTabla import crearTablaHTML

def construirDataFrameCalidadRuido():
    datosCalidadRuido=generarDatosRuido()

    calidadRuidoDF=pd.DataFrame(datosCalidadRuido, columns=['comuna','ttlpoblacion', 'tmñmuestra','decibeslenoche','decibesledia','fchaencuesta','nombre','id','nombreedificio'])

    #print(calidadRuidoDF)
    #crearTablaHTML(calidadRuidoDF,"calidadRuido")

    #Agrupando datos 
    datosAgrupados=calidadRuidoDF.groupby("comuna")["id"].mean()
   
   #Graficando datos 
    plt.figure(figsize=(20,20))
    datosAgrupados.plot(kind='bar',color='green')
    plt.title('Calidad de ruido por comuna en Medellin')
    plt.xlabel('comuna')
    plt.ylabel('ID ')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig('./assets/img/calidadRuido.png',format='png',dpi=600)
   #plt.show()

construirDataFrameCalidadRuido()

