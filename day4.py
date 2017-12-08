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
                listaLinea = linea.strip().rsplit()
                matrizCasosTest.append(listaLinea)
        fichero.close()
        
        try:
            assert len(matrizCasosTest) > 0
        except AssertionError:
            print("matriz vacía!")
        return matrizCasosTest




def validadorContraseñaFrase(matrizCasosTest):
    numeroValidas=0
    
    for frase in matrizCasosTest:
        fraseValida=True
        for palabra in frase:
            if frase.count(palabra)>1:
                fraseValida=False
        if fraseValida:
            numeroValidas+=1

    return numeroValidas

def validadorContraseñaFrase2(matrizCasosTest):
    numeroValidas=0
    
    for frase in matrizCasosTest:
        fraseValida=True
        for index,palabra in enumerate(frase):
            for index2, palabra2 in enumerate(frase):
                if index!=index2 and sorted(palabra)==sorted(palabra2):
                    fraseValida=False
        if fraseValida:
            numeroValidas+=1

    return numeroValidas

if __name__ == "__main__":

    matrizCasosTest=cargarDatosTest("/home/ulises/Micarpeta/proyectos/AdventOfCode/test4.txt")
    print(validadorContraseñaFrase(matrizCasosTest))
    print(validadorContraseñaFrase2(matrizCasosTest))