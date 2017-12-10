def cargarDatosTest(rutaAccesoFichero,matrizCasosTest=[]):
    
    
    assert isinstance(matrizCasosTest, list)
    
    try:
        if not isinstance(rutaAccesoFichero, str):
            raise ValueError
        fichero = open(rutaAccesoFichero, 'r')
    except FileNotFoundError:
        
        print("Fichero no encontrado")
        return []
    except ValueError:
        
        print("El nombre del fichero ha de ser un string")
        return []
    else:
        
        for linea in fichero:
            
                
                matrizCasosTest.append(linea.split())
                
            
        fichero.close()
        
        try:
            assert len(matrizCasosTest) > 0
        except AssertionError:
            print("matriz vacía!")
        return matrizCasosTest

def conseguirNombreRegistros(matrizCasosTest):
    registros={}
    for indice,fila in enumerate(matrizCasosTest):
        if fila[0] not in registros:
             registros[fila[0]]=0
        if fila[1] == "inc":
            matrizCasosTest[indice][1]=1
        else:
            matrizCasosTest[indice][1]=-1
        
        matrizCasosTest[indice][4]="registros['"+matrizCasosTest[indice][4]+"']"
        condicion=" ".join(matrizCasosTest[indice][4:])
        matrizCasosTest[indice]=[fila[0],int(fila[1])*int(fila[2]),condicion]
        
    return registros
def ejecutarOrdenes(matrizCasosTest,registros):
    maximo=0
    for fila in matrizCasosTest:
        
        if eval(fila[2]):
            registros[fila[0]]=registros[fila[0]]+fila[1]
        if maximoValorRegistros(registros)>maximo:
            maximo=maximoValorRegistros(registros)
    return registros,maximo

def maximoValorRegistros(registros):
    return(max(registros.values()))

if __name__ == "__main__":
    matrizCasosTest=cargarDatosTest("/home/ulises/Micarpeta/proyectos/AdventOfCode/test8.txt")
    registros=conseguirNombreRegistros(matrizCasosTest)
    resultadoOrdenes=ejecutarOrdenes(matrizCasosTest,registros)
    registros=resultadoOrdenes[0]
    maximoHistorico=resultadoOrdenes[1]
    print(registros)
    print(maximoHistorico)
   
    print(maximoValorRegistros(registros))