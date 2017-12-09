



def redistribuirMemoria(bancosMemoriaTest):

    pasos=0
    estados=[]
    Done=False
    while not Done :
        
        estados.append(list(bancosMemoriaTest))
        #print(bancosMemoriaTest,Done, estados)
        maximoBancos=max(bancosMemoriaTest)
        indiceMax=bancosMemoriaTest.index(maximoBancos)
        bancosMemoriaTest[indiceMax]=0
        while maximoBancos>0:
            #print(maximoBancos)
            #print(bancosMemoriaTest)
            if indiceMax+1>= len(bancosMemoriaTest):
                indiceMax=0
                bancosMemoriaTest[indiceMax]+=1
                maximoBancos-=1
            else:
                indiceMax+=1
                bancosMemoriaTest[indiceMax]+=1
                maximoBancos-=1
        pasos+=1
        for estado in estados:
            if estado==bancosMemoriaTest:
                Done=True
                
        #print(bancosMemoriaTest,Done, estados)
        

    return pasos

def redistribuirMemoria2(bancosMemoriaTest):
    
    pasos=0
    estados=[]
    Done=False
    while not Done :
        
        estados.append(list(bancosMemoriaTest))
        #print(bancosMemoriaTest,Done, estados)
        maximoBancos=max(bancosMemoriaTest)
        indiceMax=bancosMemoriaTest.index(maximoBancos)
        bancosMemoriaTest[indiceMax]=0
        while maximoBancos>0:
            #print(maximoBancos)
            #print(bancosMemoriaTest)
            if indiceMax+1>= len(bancosMemoriaTest):
                indiceMax=0
                bancosMemoriaTest[indiceMax]+=1
                maximoBancos-=1
            else:
                indiceMax+=1
                bancosMemoriaTest[indiceMax]+=1
                maximoBancos-=1
        pasos+=1
        for estado in estados:
            if estado==bancosMemoriaTest:
                Estadobucle=bancosMemoriaTest
                Done=True
                
        #print(bancosMemoriaTest,Done, estados)
        

    return redistribuirMemoria(Estadobucle)








if __name__ == "__main__":
    bancosMemoriaTest=[4,	10,	4,	1,	8,	4,	9,	14,	5,	1,	14,	15,	0,	15,	3,	5]
    print(redistribuirMemoria(bancosMemoriaTest))
    print(redistribuirMemoria([0, 2, 7, 0 ]))
    print(redistribuirMemoria2(bancosMemoriaTest))
