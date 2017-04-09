#%una volta che esiste una tangente, viene attivata questa funzione
def lunghezzedelnocciolo(areatotale,baricentrototalex,baricentrototaley,\
                         puntoiniziale,puntofinale,inerzia_x,inerzia_y,inerzia_xy,kappa):
    import numpy as np
    printa=0
    #%funzione che calcola l'antipolo in base alla retta scelta
    #%arrotondo l'inerziaxy alla quarta cifra, gli altri parametri vanno bene anche così
    inerzia_xy=round(inerzia_xy,kappa)
    coordx1=puntoiniziale[0,0]-baricentrototalex
    coordy1=puntoiniziale[0,1]-baricentrototaley
    coordx2=puntofinale[0,0]-baricentrototalex
    coordy2=puntofinale[0,1]-baricentrototaley
    deltax=coordx2-coordx1
    deltay=coordy2-coordy1
    alfa=0.
    beta=0.
    gamma=0.
    delta=0.
    epsilon=0.
    #%fprintf('%6.4f %6.4f %6.4f %6.4f %6.4f %6.4f \n',coordx1,coordx2,deltax,coordy1,coordy2,deltay);
    #%calcolo dei parametri delle rette tangenti, i quali finiranno nell'equazione dell'antipolo
    tipologia=np.matrix("0. 0. 0.")
    if deltax==0:
        #%tipologia='x=costante';
        #%retta di equazione x=coordx1
        alfa=-1/(coordx1)
        beta=0
        gamma=coordx1+baricentrototalex
        delta=-1/coordx1
        tipologia[0,0]=1
        tipologia[0,1]=gamma
        tipologia[0,2]=delta
    elif deltay==0:
        #%tipologia='y=costante';
        #%retta di equazione y=coordy1
        alfa=0
        beta=-1/(coordy1)
        #%non so perché ma ho dovuto mettere un meno che non sapevo
        gamma=coordy1+baricentrototaley
        delta=-1/coordy1
        tipologia[0,0]=2
        tipologia[0,1]=gamma
        tipologia[0,2]=delta
    else:
        #%retta di equazione ax+by+1=0
        #%tipologia='ax+by+1=0';
        fractor=(-coordx1*coordy2+coordx2*coordy1)
        alfa=(coordy2-coordy1)/fractor
        beta=(coordx1-coordx2)/fractor
        coordx1=coordx1+baricentrototalex
        coordy1=coordy1+baricentrototaley
        coordx2=coordx2+baricentrototalex
        coordy2=coordy2+baricentrototaley
        gamma=(coordy2-coordy1)
        delta=(coordx1-coordx2)
        epsilon=(-coordx1*coordy2+coordx2*coordy1)
        tipologia[0,0]=gamma
        tipologia[0,1]=delta
        tipologia[0,2]=epsilon
    #%dopo aver calcolato tutti i parametri che finiranno nell'equazione del calcolo dell'antipolo,
    #%posso calcolare le coordinate dell'antipolo (direttamente nel sistema di riferimento xy iniziale.
    coordxnocciolo=(alfa*inerzia_y+beta*inerzia_xy)/areatotale+baricentrototalex
    coordynocciolo=(alfa*inerzia_xy+beta*inerzia_x)/areatotale+baricentrototaley
    if printa:
        print("ccccc",alfa,inerzia_xy,beta,inerzia_x,areatotale,baricentrototaley)
        #print(coordx1,coordy1,coordx2,coordy2,deltax,deltay,coordxnocciolo,coordynocciolo)
        print("aha",type(coordynocciolo),coordynocciolo)
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    return coordxnocciolo,coordynocciolo,tipologia

def nocciolodiinerzia(listadicoordinatefinale,\
                                           baricentrototalex,baricentrototaley,\
                                           areatotale,matrice_inerzia_totale):
#function [noccioloordinato]=nocciolodiinerzia(listadicoordinatefinale,baricentrototalex,baricentrototaley,areatotale,matrice_inerzia_totale)
#%funzione che stabilisce quale retta è tangente alla figura e se vero, richiama la funzione che ne calcola l'antipolo
    #import matplotlib.pyplot as plt
    #plt.figure()
    #plt.clf()
    printa=0
    if printa:
        print(listadicoordinatefinale)
    from calcolatrice.misuras import size2,UnireMatriciRig
    import numpy as np
    kappa=6
    kappa2=2
    #print(listadicoordinatefinale)
    righe=size2(listadicoordinatefinale,1)
    inerzia_y=matrice_inerzia_totale[0,0]
    inerzia_xy=matrice_inerzia_totale[0,1]
    inerzia_x=matrice_inerzia_totale[0,3]
    #print(inerzia_y,inerzia_xy,inerzia_x)
    ff1=np.asmatrix(np.zeros((size2(listadicoordinatefinale,1),size2(listadicoordinatefinale,2))))
    listadicoordinatefinale=UnireMatriciRig(listadicoordinatefinale,ff1)
    punti=0
    if printa:
        print(listadicoordinatefinale)
    #%%%% metodo del calcolo delle tangenti, senza il raddoppio dei confronti dei punti tra di loro
    coordinatedelnocciolo=np.matrix("0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.")
    #%quante rettte indica le rette uniscono due punti presi in tutte le figure
    #%quanterette=(righe*(righe-1))/2
    from calcolatrice.misuras import rototrasl,angolopolarecartesiano,arrotonda,minimo,massimo,UnireMatriciCol
    VetRighe=range(0,righe-1)
    VetRighe1=range(0,righe)
    puntoiniziale=np.matrix("0. 0.")
    puntofinale=np.matrix("0. 0.")
    dex=0.
    dey=0.
    tipologia=np.matrix("0. 0. 0.")
    coordxnocciolo=0.
    coordynocciolo=0.
    for i in VetRighe:
        VetRighe2=range(i+1,righe)
        for j in VetRighe2:
            puntoiniziale[0,0]=listadicoordinatefinale[i,0]
            puntoiniziale[0,1]=listadicoordinatefinale[i,1]
            puntofinale[0,0]=listadicoordinatefinale[j,0]
            puntofinale[0,1]=listadicoordinatefinale[j,1]
            deltax=puntofinale[0,0]-puntoiniziale[0,0]
            deltay=puntofinale[0,1]-puntoiniziale[0,1]
            angolo_rad=angolopolarecartesiano(deltax,deltay)
            dex=puntoiniziale[0,0]
            dey=puntoiniziale[0,1]	
            for k in VetRighe1:
                xdarototraslare=listadicoordinatefinale[k,0]
                ydarototraslare=listadicoordinatefinale[k,1]
                xrototraslato,yrototraslato=rototrasl(xdarototraslare,ydarototraslare,dex,dey,angolo_rad,"1")
                ff1[k,0]=xrototraslato
                ff1[k,1]=yrototraslato
                #%si potrebbe agire qui, controllando ogni volta che il punto sia negativo o positivo,
                #%si creano due variabili, una per i numeri positivi e una per i numeri negativi
                #%e ogni volta che si ottiene un risultato si somma 1 a quella giusta
                #%ogni volta si controlla se una è zero e l'altra no
                #%se tutte e due sono diverse da zero, allora la tangente non è tale
                #è un metodo meno oneroso di quello che sto usando ora?
                #%listadicoordinatefinale(:,4)
                #listadicoordinatefinale[:,3]=arrotonda(listadicoordinatefinale[:,3],kappa)
                vettoremassimieminimi=arrotonda(ff1[:,1],kappa)
                puntominimo=minimo(vettoremassimieminimi)
                puntomassimo=massimo(vettoremassimieminimi)
#####################################################################################
                #print("ccc",puntominimo,puntomassimo)
            cacca=np.matrix("0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.")
            if printa:
                print(listadicoordinatefinale)
            #se passano questo if allora sono delle tangenti
            ver1=(puntomassimo>=0 and puntominimo>=0)
            ver2=(puntomassimo<=0 and puntominimo<=0)
            if ver1+ver2==1:
                ##############################
                # puntoiniziale 1x2 puntofinale 1x2
                if punti==0:
                    coordinatedelnocciolo=np.matrix("0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.")
                else:
                    coordinatedelnocciolo=UnireMatriciCol(coordinatedelnocciolo,cacca)
                coordxnocciolo=0.
                coordynocciolo=0.
                coordxnocciolo,coordynocciolo,tipologia=lunghezzedelnocciolo(areatotale,baricentrototalex,baricentrototaley,puntoiniziale,puntofinale,inerzia_x,inerzia_y,inerzia_xy,kappa)
                #[coordxnocciolo,coordynocciolo,tipologia]=lunghezzedelnocciolo(areatotale,baricentrototalex,baricentrototaley,puntoiniziale,puntofinale,inerzia_x,inerzia_y,inerzia_xy);
                # tipologia matrice 1x3
                if printa:
                    print(coordinatedelnocciolo)
                    print(type(coordinatedelnocciolo))
#####################################################################################
                    print(coordxnocciolo,coordynocciolo[0,0],deltax,deltay,baricentrototalex,baricentrototaley)
                coordinatedelnocciolo[punti,0]=coordxnocciolo[0,0]
                if printa:
                    print("coordynocciolo",coordynocciolo,np.size(coordynocciolo),"ops1",coordinatedelnocciolo[punti,1])
                    print(type(coordxnocciolo),type(coordynocciolo))
                if punti==0:
                    coordinatedelnocciolo[punti,1]=coordynocciolo[0,0]
                else:
                    coordinatedelnocciolo[punti,1]=coordynocciolo[0,0]
                if printa:
                    print("ops",coordinatedelnocciolo[punti,1])
                coordinatedelnocciolo[punti,2]=punti+1
                deltax=coordxnocciolo-baricentrototalex
                deltay=coordynocciolo-baricentrototaley
                theta=angolopolarecartesiano(deltax,deltay)
                coordinatedelnocciolo[punti,3]=theta
                coordinatedelnocciolo[punti,4]=puntoiniziale[0,0]
                coordinatedelnocciolo[punti,5]=puntoiniziale[0,1]
                coordinatedelnocciolo[punti,6]=puntofinale[0,0]
                coordinatedelnocciolo[punti,7]=puntofinale[0,1]
                coordinatedelnocciolo[punti,8]=tipologia[0,0]
                coordinatedelnocciolo[punti,9]=tipologia[0,1]
                coordinatedelnocciolo[punti,10]=tipologia[0,2]
                coordinatedelnocciolo[punti,11]=coordxnocciolo-baricentrototalex
                coordinatedelnocciolo[punti,12]=coordynocciolo-baricentrototaley
                punti=punti+1
                #print(pirla,puntominimo,puntomassimo,theta)
                #a=listadicoordinatefinale[i,0]
                #b=listadicoordinatefinale[i,1]
                #c=listadicoordinatefinale[j,0]
                #d=listadicoordinatefinale[j,1]
                #print(a,b,c,d)
                    #%coordinatedelnocciolo(punti,5)=tipologia;
                #%fprintf('%6.0f %6.0f %6.0f %6.0f \n',coordinatedelnocciolo(punti,5),coordinatedelnocciolo(punti,6),coordinatedelnocciolo(punti,7),coordinatedelnocciolo(punti,8));
                #end
                if printa:
                    print(coordinatedelnocciolo)
    #end
    #print(coordinatedelnocciolo.T)
    #if printa:
    if printa:
        print(coordinatedelnocciolo.T)          
    coordinatedelnocciolo[:,0]=arrotonda(coordinatedelnocciolo[:,0],kappa)
    coordinatedelnocciolo[:,1]=arrotonda(coordinatedelnocciolo[:,1],kappa)
    #end
    if printa:
        print(coordinatedelnocciolo[:,0:2])
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%coordinatedelnocciolo sono inserite in un file di testo
    #%vedere di fare una stampata di latex cos?? da segnalare in modo leggibile tutti i punti
    #%plot(coordinatedelnocciolo(:,1),coordinatedelnocciolo(:,2))
    #%coordinatedelnocciolo(punti,1)=coordxnocciolo;
    #%coordinatedelnocciolo(punti,2)=coordynocciolo;
    #%coordinatedelnocciolo=arrotondadecimali(coordinatedelnocciolo);
    #%funzione che ordina le righe della matric, in base alla colonna degli angoli theta
    #print(nocciolosenzadoppie.T)
    #print(coordinatedelnocciolo)
    #%penso che non c'è bisogno di ricavarla di nuovo, in fin dei conti la ho gia'
    punti=size2(coordinatedelnocciolo,1)
    matricina=arrotonda(coordinatedelnocciolo[:,3],kappa)
    matricina.sort(axis=0)
    from calcolatrice.misuras import CancDoppioni
    matricina=CancDoppioni(matricina)
    #noccioloordinato=np.asmatrix(np.zeros((r1,r2)))
    #%codice che ordina la lista di punti in base all'angolazione antioraria a partire dall'asse x positivo
    trovate=np.asmatrix(np.zeros((size2(matricina,1),13)))
    #print(matricina)
    VetPunti=range(0,punti)
    VetTro=range(0,size2(matricina,1))
    #print(VetTro)
    for i in VetTro:
        angoloscelto=matricina[i,0]
        for j in VetPunti:
            angoloj=round(coordinatedelnocciolo[j,3],kappa)
            #print(angoloscelto,angoloj)
            if angoloj==angoloscelto:
                trovate[i,:]=coordinatedelnocciolo[j,:]
    """
    #print("kappa",size2(trovate,1),size2(trovate,2))
    if size2(trovate,1)>1:
        VetKappa=range(0,size2(trovate,1),size2(trovate,2))
        for k in VetKappa:
            noccioloordinato[i,:]=nocciolosenzadoppie[trovate[k,0],:]
    else:
        noccioloordinato[i,:]=nocciolosenzadoppie[trovate[0,0],:]
    """
     #print(trovate)
    #%metodo per cancellare i doppioni
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    return trovate