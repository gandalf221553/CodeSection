def codicesezione(self):
    #%attivazione diretta del calcolatore (tutti e 3 arrivano a questo punto,
    #%ma con la scelta 1 ci si arriva senza passaggi intermedi
    import numpy as np
    from calcolatrice.studiatore2 import studianumero1
    printa=0

    #from misuras import StringaToMatrix,StringCnf
    #print(type(numero0))
    #ossas="<class 'str'>"
    #if StringCnf(type(numero0),ossas):
    #else:
    #    numero1=np.asmatrix(numero0)
    #print(type(self))
    from calcolatrice.misuras import StringCnf
    prova=str(type(self))
    prova2=str("<class 'numpy.matrixlib.defmatrix.matrix'>")
    #in pratica se voglio fare le prove non faccio i disegni
    testare=1
    #se prove =1 allora disegno, altrimenti no
    if StringCnf(prova,prova2):
        numero1=self
        testare=0
    else:
        numero1=self.stringa
    #if printa:
    np.set_printoptions(threshold=np.nan)

    if printa:
        print(type(numero1))
    if type(numero1)=="<class 'numpy.matrixlib.defmatrix.matrix'>":
        print("il tipo di oggetto va bene")
    else:
        #type()==array
        numero1=np.asmatrix(numero1)
    verz=numero1[0,0]
    #print("verz",verz)
    if printa:
        if verz==042015.:
            print("verz confermata",verz)
        else:
            print("Il codice di versione non corrisponde, il file non è valido\n")
    kk=numero1[0,1]	                                         #non deve essere mai minore di 2
    if kk>3 and kk<20:
        kk=3		
        print("kk",kk)  		                              #standard 2
    vuoifareancheilnocciolo=numero1[0,2]	                  #uguale a 1 se vuoi fare, uguale a 0 se non lo vuoi fare
    if vuoifareancheilnocciolo==0 or vuoifareancheilnocciolo==1:
        if printa:
            print("vuoifareancheilnocciolo",vuoifareancheilnocciolo)
    else:
        vuoifareancheilnocciolo=0 #standard 0
    discretizzaarchicerchi=numero1[0,3]	#standard 50
    if printa:
        print("discretizzaarchicerchi",discretizzaarchicerchi)
    if discretizzaarchicerchi<4 or discretizzaarchicerchi>100:
        discretizzaarchicerchi=30
    contorna=numero1[0,4]	#%standard 1
    if contorna==0. or contorna==1.:
        if printa:
            print("contorna conf",contorna)
    else:
        contorna=0
    from calcolatrice.misuras import size2 #, EstraiUnPezzo
    sollecitazione=np.asmatrix(np.zeros((1,8)))
    if size2(numero1,2)>=14:
        sollecitazione=np.transpose(numero1[0,5:13])
    if printa:
        print("numerotrasla",numero1)
    numero1=np.delete(numero1, (0), axis=0)
    #numero1=np.asmatrix(EstraiUnPezzo(numero1,1,"end",0,"end"))
    if printa:
        print("numerotrasla",numero1)  
    #numero1=numero1([2:end,:]
    if printa:
        print("aa1")
    #%questo sarebbe il programma principale di calcolo dell'inerzia
    numerodifiguregeneriche=size2(numero1,1) #% dimmi quante figure vuoi inserire
    #print("numfiggen",numerodifiguregeneriche)
    #%cerca di calcolare i parametri xy tali da traslare tutte le figure in un sistema di riferimento positivo
    calcolo=2
    traslax=0
    traslay=0
    VetRigheGen=range(0,numerodifiguregeneriche)    #print("VetRigheGen",VetRigheGen)
    if printa:
        print("aa2")
    for k in VetRigheGen:
        #[~,~,~,~,~,~,minimox,minimoy,~,~]=studiatore2()
        #print(type(np.asmatrix(numero1[k,:])))
        #print("numerok",numero1[k,:],size2(numero1[k,:],1),size2(numero1[k,:],2))
        riganumer=np.asmatrix(numero1[k,:])
        coordinate,c1,c2,c3,c4,c5,minimox,minimoy,c8,c9=studianumero1(riganumer,kk,calcolo,0,0,0)
        traslax=np.minimum(traslax,minimox)
        traslay=np.minimum(traslay,minimoy)
    if printa:
        print("numerotrasla",numero1)        
    if printa:
        print("aa3")
    #%per sicurezza aumenta di 2
    traslax=-traslax+2
    traslay=-traslay+2
    #print("traslax",traslax)
    #print("traslay",traslay)
    #print("traslax",traslax)
    #print("traslay",traslay)
    calcolo=3
    """
    %traslax=8000;			%il 20000 #porta un errore che si nota
    %traslay=traslax;		
    #%non modificare"""
    #print(VetRigheGen)
    numero4=numero1
    #print(numero4.T)
    for i in VetRigheGen:
        #print("numero4 33", i,numero1[i,:])
        numero33=np.asmatrix(numero1[i,:])
        #print(type(numero33))
        b1,b2,b3,b4,b5,b6,b7,b8,numero4[i,:],b9=studianumero1(numero33,kk,calcolo,0,traslax,traslay)
        #[~,~,~,~,~,~,~,~,numero4,~]=studiatore2()5
        #print("numero4", numero4)
    from calcolatrice.xgeom2 import xgeom
    #%calcolo dei parametri geometrici della sezione
    #print(transponi(numero4))
    if printa:
        print("numero4",numero1)
        
    areatotale,baricentrototalex,baricentrototaley,essex,essey,matrice_inerzia_totale,Aangolo_rad,Aangolo_gon,angolo_rad,Aangolo_grad,rhoeee,rhonii,casoinesame,inerziaeee,inerzianii=xgeom(numero4,kk)
    
    if printa:
        print("cacca")
        print(areatotale)
        print(baricentrototalex)
        print(baricentrototaley)
        #print(vettore_baricentrix)
        #print(vettore_baricentriy)
        print(essex)
        print(essey)
        #print(vet_m_inerzia_huygens)
        print(matrice_inerzia_totale)
        print(Aangolo_rad)
        print(Aangolo_gon)
        print(Aangolo_grad)
        print(rhoeee)
        print(rhonii)
        print(casoinesame)
        print(inerziaeee)
        print(inerzianii)
    #%fprintf('#####');
    #%fprintf('#####');
    """%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %metodo per scoprire la lista delle coordinate, per calcolare il massimo e il minimo"""
    from calcolatrice.misuras import listare,CancDoppioni
    listadicoordinatefinale=listare(numero1,kk,discretizzaarchicerchi)
    #print(size2(listadicoordinatefinale,1))
    #print(listadicoordinatefinale)
    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
    listadicoordinatefinale=CancDoppioni(listadicoordinatefinale)
    #se c'e almeno una figura vuo5ta fai il calcolo peso
    if printa:
        print("casfnhedhbvsehbvsedv")
    if 1:
        contorna=0
        for ps in VetRigheGen:
            if numero1[ps,1]<0:
                contorna=1 #cambialo a 1 poi
                #per evidente semplicità non ho voglia di fare anche questo calcolatore
                ps=numerodifiguregeneriche
        if contorna:
            from calcolatrice.contornalacomposizione import contorna
            listadicoordinatefinale=contorna(listadicoordinatefinale,numero1,kk,discretizzaarchicerchi)
    matrice_inerzia_totale=np.asmatrix(matrice_inerzia_totale)
    #print(listadicoordinatefinale)
    #print(listadicoordinatefinale)
    numeri=size2(listadicoordinatefinale,1)
    VetLista=range(0,numeri)
    for t in VetLista:
        #print(t)
        listadicoordinatefinale[t,0]=listadicoordinatefinale[t,0]-traslax
        listadicoordinatefinale[t,1]=listadicoordinatefinale[t,1]-traslay
    baricentrototalex=baricentrototalex-traslax
    baricentrototaley=baricentrototaley-traslay
    essey=areatotale*baricentrototalex
    essex=areatotale*baricentrototaley
    """%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""
    if vuoifareancheilnocciolo:
        """
        %visto la quantità di calcoli richiesti, lascio la possibilit di scelta??
        """
        #print(listadicoordinatefinale,baricentrototalex,baricentrototaley,areatotale,matrice_inerzia_totale)
        from calcolatrice.nocciolo import nocciolodiinerzia
        noccioloordinato=nocciolodiinerzia(listadicoordinatefinale,\
                                           baricentrototalex,baricentrototaley,\
                                           areatotale,matrice_inerzia_totale)
        #%nel noccioloordinato coordinate #del nocciolo ordinate in senso #antiorario a partire da x positivo
        #noccioloordinato=np.matrix("0 0 0 0 0 0 0 0 0 0 0 0 0;1 1 1 1 1 1 1 1 1 1 1 1 1; 2 2 2 2 2 2 2 2 2 2 2 2 2")
    else:
        noccioloordinato=-1
    #print(listadicoordinatefinale)
    #%%%%%%%%%%%%%%%%%%%%%%%%
    #print(sollecitazione)
    if sollecitazione[0,0]==1. or sollecitazione[0,0]==2.:
        #x.sollecitazione=sollecitazione
        #vettore_baricentrix=vettore_baricentrix-traslax
        #vettore_baricentriy=vettore_baricentriy-traslay
        #baricentrototalex=baricentrototalex-traslax
        #baricentrototaley=baricentrototaley-traslay
        from calcolatrice.spinte import sollecitatore
        #string=stampacalcoli()
        
        puntopiulontanoyyy1,puntopiulontanoxxx1,puntopiulontanoyyy2,puntopiulontanoxxx2,sigmadelpuntopiulontano1,sigmadelpuntopiulontano2,tresca,mises=sollecitatore(sollecitazione,angolo_rad,Aangolo_rad,\
                      listadicoordinatefinale,areatotale,baricentrototalex,\
                      baricentrototaley,rhonii,rhoeee,inerzianii,inerziaeee)
    else:
        puntopiulontanoyyy1=0
        puntopiulontanoxxx1=0
        puntopiulontanoyyy2=0
        puntopiulontanoxxx2=0
        sigmadelpuntopiulontano1=0
        sigmadelpuntopiulontano2=0        
    

    from calcolatrice.risultatileggibili import RisToString
    #risultatitxt(x,noccioloordinato)
    #areatotale,baricentrototalex,baricentrototaley,essex,essey,matrice_inerzia_totale,Aangolo_rad,Aangolo_gon,Aangolo_grad,rhoeee,rhonii,casoinesame,inerziaeee,inerzianii
    stringa=RisToString(noccioloordinato,vuoifareancheilnocciolo,areatotale,baricentrototalex,baricentrototaley,essex,essey,matrice_inerzia_totale,Aangolo_rad,Aangolo_gon,Aangolo_grad,rhoeee,rhonii,casoinesame,inerziaeee,inerzianii)
    #print(noccioloordinato)
        #%%%%%%%%%%%%%%%%%%%%%%%%
    if printa:
        print("cacca")
        print("areatotale",areatotale)
        print("barix",baricentrototalex)
        print("bariy",baricentrototaley)
        #print(vettore_baricentrix)
        #print(vettore_baricentriy)
        print("essex",essex)
        print("essey",essey)
        #print(vet_m_inerzia_huygens)
        print("inerzia",matrice_inerzia_totale)
        print("angolo_rad",angolo_rad)
        print("Aangolo_gon",Aangolo_gon)
        print("Aangolo_grad",Aangolo_grad)
        print("rhoeee",rhoeee)
        print("rhonii",rhonii)
        print("casoinesame",casoinesame)
        print("inerziaeee",inerziaeee)
        print("inerzianii",inerzianii)
    #per disegnare
    #nomArch="ciccione"
    if testare:
        for t in VetLista:
            #print(t)
            listadicoordinatefinale[t,0]=listadicoordinatefinale[t,0]+traslax
            listadicoordinatefinale[t,1]=listadicoordinatefinale[t,1]+traslay
        baricentrototalex=baricentrototalex+traslax
        baricentrototaley=baricentrototaley+traslay
    if vuoifareancheilnocciolo:
        quantecoordinatenocciolo=size2(noccioloordinato,1)
        VetListaNocc=range(0,quantecoordinatenocciolo)
        for t in VetListaNocc:
            #print(t)
            noccioloordinato[t,0]=noccioloordinato[t,0]+traslax
            noccioloordinato[t,1]=noccioloordinato[t,1]+traslay
        from calcolatrice.plottare import poltrire
        poltrire(self,numero1,kk,discretizzaarchicerchi,vuoifareancheilnocciolo\
                 ,noccioloordinato,listadicoordinatefinale,traslax,traslay,\
                 sollecitazione,baricentrototalex,baricentrototaley,Aangolo_rad,\
                 rhonii,rhoeee,puntopiulontanoyyy1,puntopiulontanoxxx1,\
                 puntopiulontanoyyy2,puntopiulontanoxxx2,sigmadelpuntopiulontano1,\
                 sigmadelpuntopiulontano2,angolo_rad)
    if printa:
        print(stringa)
    #plottare(numero1,kk,nomArch,discretizzaarchicerchi,vuoifareancheilnocciolo,noccioloordinato,listadicoordinatefinale,traslax,traslay,sollecitazione,x)
    return stringa
