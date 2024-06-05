import pandas as pd 

from data.generators.generadorruido import generarDatosRuido
from helpers.generarTabla import crearTablaHTML

def construirDataFrameCalidadRuido():
    datosCalidadRuido=generarDatosRuido()

    calidadRuidoDF=pd.DataFrame(datosCalidadRuido, columns=['comuna','ttlpoblacion', 'tmñmuestra','decibeslenoche','decibesledia','fchaencuesta','nombre','id','nombreedificio'])

    print(calidadRuidoDF)
    crearTablaHTML(calidadRuidoDF,"calidadRuido")

construirDataFrameCalidadRuido()

