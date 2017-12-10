def cargarDatosTest(rutaAccesoFichero,matrizCasosTest={}):
    
    
    assert isinstance(matrizCasosTest, dict)
    
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
                listaLinea=linea.split()
                
                matrizCasosTest[listaLinea[0]]=[int(listaLinea[1][1:-1])," ".join(listaLinea[3:]).split(", ")]
                
            except IndexError:
                print(linea)
        fichero.close()
        
        try:
            assert len(matrizCasosTest) > 0
        except AssertionError:
            print("matriz vacía!")
        return matrizCasosTest

def definidorRaiz(matrizCasosTest):
    listaSubelementos=[]
    for value in matrizCasosTest.values():
        for subelemento in value[1]:
            listaSubelementos.append(subelemento)
    
    for key, valor in matrizCasosTest.items():
        if valor[1]!=[] and key not in listaSubelementos:
            
            raiz=key
    return raiz


    matrizraiz={}
    submatriz=[]
    listatest=list(matrizCasosTest.items())
    indice=0
    while indice<len(listatest):
        testkey=listatest[indice][0]
        for key, value in listatest:
            if testkey in value[1]:
                pesoEsperado=matrizCasosTest[testkey][0]
                for llave in value[1]:
                    
                    if matrizCasosTest[llave][0]!=pesoEsperado:
                        return (pesoEsperado,abs(matrizCasosTest[llave][0]-pesoEsperado))
        indice=indice+1


def findstructure(matrizCasosTest, raiz):
    
    
    if matrizCasosTest[raiz][1]==[] or matrizCasosTest[raiz][1]==[""]:
        return matrizCasosTest[raiz][0]
    else:
       
        for programa in matrizCasosTest[raiz][1]:
            #matrizCasosTest[key].insert(0,value[-2]+pesoEsperado*(len(value[-1]))
            matrizCasosTest[raiz].append(findstructure(matrizCasosTest,programa))
        
        if len(matrizCasosTest[raiz])==len(matrizCasosTest[raiz][1])+2:
            suma=0
            for atributo in matrizCasosTest[raiz]:
                if isinstance(atributo,int):
                    suma=suma+atributo
            matrizCasosTest[raiz].append(suma)
            return suma
    
def encuentraDesequilibrio(matrizCasosTest):
    programaError=None
    for programas, atributos in matrizCasosTest.items():
        if len(atributos)>2:
            for atributo in atributos[2:-1]:
                if len(atributos[2:-1])==2 and atributos[2:-1][0]!=atributos[2:-1][1] :
                    print("WTF")
                    programaError=atributos[1][0]
                elif atributos[2:-1].count(atributo)==1:
                    print (programas,atributos[1],atributos[2:-1],atributos[-1])
                    
                    if programaError is None:
                        programaError=atributos[1][atributos[2:-1].index(atributo)]
                        deepflag=atributos[-1]
                        pesos=set(atributos[2:-1])
                        pesoError=atributo
                    else:
                        if atributos[-1]<deepflag:
                          programaError=atributos[1][atributos[2:-1].index(atributo)]  
                          deepflag=atributos[-1]
                          pesos=set(atributos[2:-1])
                          pesoError=atributo
    for peso in pesos:
        if pesoError-peso>0:
            return matrizCasosTest[programaError][0]-(pesoError-peso)
        elif pesoError-peso<0:
            return matrizCasosTest[programaError][0]+(pesoError-peso)
              


    

if __name__ == "__main__":
    matrizCasosTest=cargarDatosTest("/home/ulises/Micarpeta/proyectos/AdventOfCode/test7.txt")
    print(definidorRaiz(matrizCasosTest))
    raiz=definidorRaiz(matrizCasosTest)
    findstructure(matrizCasosTest,raiz)
    print(encuentraDesequilibrio(matrizCasosTest))
    #print(checkPesoEquilibrado2(matrizCasosTest,raiz))

    #for key, value in matrizCasosTest.items():
    #    print(key, value,"\n")

    matrizCasosTest={}
    matrizCasosTest["pbga"]= [66,[]]
    matrizCasosTest["xhth"]= [57,[]]
    matrizCasosTest["ebii"]= [61,[]]
    matrizCasosTest["havc"] =[66,[]]
    matrizCasosTest["ktlj"] =[57,[]]
    matrizCasosTest["fwft"] =[72,  ["ktlj", "cntj", "xhth"]]
    matrizCasosTest["qoyq"] =[66,[]]
    matrizCasosTest["padx"] =[45,  ["pbga", "havc", "qoyq"]]
    matrizCasosTest["tknk"] =[41,  ["ugml", "padx", "fwft"]]
    matrizCasosTest["jptl"] =[61,[]]
    matrizCasosTest["ugml"] =[68, ["gyxo", "ebii", "jptl"]]
    matrizCasosTest["gyxo"] =[61,[]]
    matrizCasosTest["cntj"] =[57,[]]
    print(matrizCasosTest)
    raiz=definidorRaiz(matrizCasosTest)
    print(raiz)
    print(findstructure(matrizCasosTest,raiz))
    print(encuentraDesequilibrio(matrizCasosTest))