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
            try:
                
                matrizCasosTest.append(int(linea[:-1]))
            except ValueError:
                print(linea[:-1])
        fichero.close()
        
        try:
            assert len(matrizCasosTest) > 0
        except AssertionError:
            print("matriz vacía!")
        return matrizCasosTest

def locuraInstruccion(matrizCasosTest):
    
    pasos=0
    indice=0
    salto=0
    while indice<len(matrizCasosTest):
        salto=matrizCasosTest[indice]
        matrizCasosTest[indice]=matrizCasosTest[indice]+1
        indice=indice+salto
        pasos+=1
    return pasos

def locuraInstruccion2(matrizCasosTest):
    
    pasos=0
    indice=0
    salto=0
    while indice >= 0 and indice<len(matrizCasosTest):
        
        salto=matrizCasosTest[indice]
        if matrizCasosTest[indice]>=3:
            matrizCasosTest[indice]=matrizCasosTest[indice]-1
        else:
            matrizCasosTest[indice]=matrizCasosTest[indice]+1
        indice=indice+salto
        pasos+=1
    return pasos
        
if __name__ == "__main__":
    #matrizCasosTest=cargarDatosTest("/home/ulises/Micarpeta/proyectos/AdventOfCode/test5.txt")
    #print(locuraInstruccion(matrizCasosTest))
    matrizCasosTest=cargarDatosTest("/home/ulises/Micarpeta/proyectos/AdventOfCode/test5.txt")
    print(locuraInstruccion2(matrizCasosTest))
    print(locuraInstruccion2([0, 3,  0,  1,  -3]))