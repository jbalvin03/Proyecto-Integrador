import random

def generarAreaArboles():
    listaDatos=[]
    for i in range(1000):
        corregimiento=random.choice(['Cacerí', 'Cuturu','El Pando,La Ilusion', 'Margento','Palanca','Palomar','Puerto Colombia'])
        nombreArbol=random.choice(['Encina','Alcornoque','Acebuche','Olivo Silvestre', 'ipuana', 'Acacia Mimosa','Limonero','Pino'])
        idArbol=random.randint(1,100)
        hectariasSenbradas=random.choice(['500','1000','2000','2500','3000'])
        FrutaArbol=random.choice(['Fresa', 'Mango', 'Manzana', 'Aguacate'])
        areaArbol=[corregimiento,nombreArbol, idArbol, hectariasSenbradas]

        listaDatos.append(areaArbol)

        

        return listaDatos
    print(generarAreaArboles())