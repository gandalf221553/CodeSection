def sollecitatore(sollecitazione,angolo_rad,Aangolo_rad,listadicoordinatefinale,areatotale,baricentrototalex,baricentrototaley,rhonii,rhoeee,inerzianii,inerziaeee):
    #function [x]=elaborazione_della_sollecitazione(x)
    #%attenzione la parte di elaboratore non capisce se una figura è stata eliminata, 
    #%quindi ci possono essere grossi problemi nel calcolo del punto più lontano
    #%se ci sono vuoti
    #%l'applivazione e stata aggiornata e ora puo calcolare efficacemente i vuoti
    #%ragion per cui la funzione e stata riaggiunta alla alpha
    
    #%c'è
    #%flessione deviata
    #%pressoflessione deviata
    
    #%cd risultati
    #%completo=csvread('datidellefiguracompleta.csv');
    #%cd ..

    import numpy as np
    from math import pi,cos,sin
    from calcolatrice.misuras import size2,UnireMatriciRig,angolopolarecartesiano
    moltiplica=1
    angolo_rad=0
    ricorda=Aangolo_rad
    ff1=np.asmatrix(np.zeros((size2(listadicoordinatefinale,1),2)))
    listadicoordinatefinale=UnireMatriciRig(listadicoordinatefinale,ff1)
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%tipo forza (1) o tipo momento (2)
    tipo=sollecitazione[0,0]
    punto_x_di_applicazione=sollecitazione[1,0]
    punto_y_di_applicazione=sollecitazione[2,0]
    trazioneocompressione=sollecitazione[3,0]
    sforzonormale=sollecitazione[4,0]
    momento=sollecitazione[5,0]
    direzionedelmomento=sollecitazione[6,0]
    tau=sollecitazione[7,0]
    #sigmamassimadiprogetto=sollecitazione[0,8]
    direzionedelmomento=direzionedelmomento/180*pi
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    #%funzione di rototraslazione del punto di applicazione
    #%c'e un errore nella funzione sotto!!!!!!!!!!!!!!!!!!!!!!!
    #%%%%%%%%%%%%%%%%%%%
    #%cd risultati
    #%listadicoordinatefinale=csvread('listadicoordinatefinale.csv');
    #%cd ..
    #%vettore delle y
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%listadicoordinatefinale
    quantecoordinate=size2(listadicoordinatefinale,1) #% dimmi quante figure vuoi inserire
    #=grandezza(1,1);
    punto_eee_di_applicazione=0
    punto_nii_di_applicazione=0
    dex=0
    dey=0
    angolo_rad=ricorda
    VetQ=range(0,quantecoordinate)
    from calcolatrice.misuras import rototrasl
    for i in VetQ:
        xdarototraslare=listadicoordinatefinale[i,0]-baricentrototalex
        ydarototraslare=listadicoordinatefinale[i,1]-baricentrototaley
        #%angolo_rad già dichiarato
        xrototraslato,yrototraslato=rototrasl(xdarototraslare,ydarototraslare,dex,dey,angolo_rad,moltiplica)
        listadicoordinatefinale[i,2]=xrototraslato
        listadicoordinatefinale[i,3]=yrototraslato
    momentonii=0
    momentoeee=0
    sigmamassima=0
    termine1=0
    termine2=0
    termine3=0
    termine4=0
    termine5=0
    attata=0
    m=0
    quella=0
    sigmadelpuntopiulontano1=0
    sigmadelpuntopiulontano2=0
    if tipo==1:
        #%rototraslazione sugli assi principali del punto di applicazione
        xdarototraslare=punto_x_di_applicazione-baricentrototalex
        ydarototraslare=punto_y_di_applicazione-baricentrototaley;
        angolo_rad=ricorda
        xrototraslato,yrototraslato=rototrasl(xdarototraslare,ydarototraslare,dex,dey,angolo_rad,moltiplica)
        punto_eee_di_applicazione=xrototraslato
        punto_nii_di_applicazione=yrototraslato
        m=-(punto_eee_di_applicazione*(rhoeee))/((rhonii)*punto_nii_di_applicazione)
        quella=-(rhoeee)/punto_nii_di_applicazione
        deltax=2-1
        deltay=(m*2+quella)-(m*1+quella)
        [theta]=angolopolarecartesiano(deltax,deltay)
        rettadelnullo=theta
        angolo_rad=rettadelnullo
        listadicoordinatefinale=UnireMatriciRig(listadicoordinatefinale,ff1)
        listadicoordinatefinale[:,4]=listadicoordinatefinale[:,2]
        listadicoordinatefinale[:,5]=listadicoordinatefinale[:,3]
        #%x.listadicoordinatefinale
        for i in VetQ:
            xdarototraslare=listadicoordinatefinale[i,2]
            ydarototraslare=listadicoordinatefinale[i,3]-quella
            xrototraslato,yrototraslato=rototrasl(xdarototraslare,ydarototraslare,dex,dey,angolo_rad,moltiplica)
            listadicoordinatefinale[i,4]=xrototraslato
            listadicoordinatefinale[i,5]=yrototraslato
    elif tipo==2:
        attata=direzionedelmomento-ricorda
        momentoeee=momento*cos(attata)
        momentonii=momento*sin(attata)
        m=(momentonii*inerziaeee/momentoeee/inerzianii)
        quella=0
        deltax=1
        deltay=m
        theta=angolopolarecartesiano(deltax,deltay)
        rettadelnullo=theta
        angolo_rad=rettadelnullo
        dex=0
        dey=0
        listadicoordinatefinale=UnireMatriciRig(listadicoordinatefinale,ff1)
        for i in VetQ:
            xdarototraslare=listadicoordinatefinale[i,2]
            ydarototraslare=listadicoordinatefinale[i,3]
            xrototraslato,yrototraslato=rototrasl(xdarototraslare,ydarototraslare,dex,dey,angolo_rad,moltiplica)
            listadicoordinatefinale[i,4]=xrototraslato
            listadicoordinatefinale[i,5]=yrototraslato
    else:
        print('ma che altri problemi?')
			

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    massimodellenii=listadicoordinatefinale[0,5]
    posizionedelmassimodellenii=1
    for i in VetQ: #2:quantecoordinate
        if listadicoordinatefinale[i,5]>massimodellenii:
            massimodellenii=listadicoordinatefinale[i,5]
            posizionedelmassimodellenii=i
    puntopiulontanoeee1=listadicoordinatefinale[posizionedelmassimodellenii,2]
    puntopiulontanonii1=listadicoordinatefinale[posizionedelmassimodellenii,3]
    puntopiulontanoxxx1=listadicoordinatefinale[posizionedelmassimodellenii,0]
    puntopiulontanoyyy1=listadicoordinatefinale[posizionedelmassimodellenii,1]
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    minimodellenii=listadicoordinatefinale[0,5]
    posizionedelminimodellenii=1
    for i in VetQ: #=2:quantecoordinate
        if listadicoordinatefinale[i,5]<minimodellenii:
            minimodellenii=listadicoordinatefinale[i,5]
            posizionedelminimodellenii=i
    puntopiulontanoeee2=listadicoordinatefinale[posizionedelminimodellenii,2]
    puntopiulontanonii2=listadicoordinatefinale[posizionedelminimodellenii,3]
    puntopiulontanoxxx2=listadicoordinatefinale[posizionedelminimodellenii,0]
    puntopiulontanoyyy2=listadicoordinatefinale[posizionedelminimodellenii,1]
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if tipo==1:
        termine1=(trazioneocompressione*sforzonormale)/areatotale
        termine2=punto_nii_di_applicazione*puntopiulontanonii1/(rhoeee)
        termine3=punto_eee_di_applicazione*puntopiulontanoeee1/(rhonii)
        termine4=punto_nii_di_applicazione*puntopiulontanonii2/(rhoeee)
        termine5=punto_eee_di_applicazione*puntopiulontanoeee2/(rhonii)
        sigmadelpuntopiulontano1=termine1*(1+termine2+termine3)
        sigmadelpuntopiulontano2=termine1*(1+termine4+termine5)
        sigmamassima=sigmadelpuntopiulontano1
        if sigmamassima>sigmadelpuntopiulontano2:
            sigmamassima=sigmadelpuntopiulontano2
    elif tipo==2:
        #%funzione che richiama il calcolo del momento
        #x.termine1=0;
        #%fprintf('momentoeee')
        termine2=momentoeee/inerziaeee*puntopiulontanonii1
        termine3=momentonii/inerzianii*puntopiulontanoeee1
        termine4=momentoeee/inerziaeee*puntopiulontanonii2
        termine5=momentonii/inerzianii*puntopiulontanoeee2
        sigmadelpuntopiulontano1=termine1+termine2-termine3
        sigmadelpuntopiulontano2=termine1+termine4-termine5
        sigmamassima=np.abs(sigmadelpuntopiulontano1)
        if np.abs(sigmadelpuntopiulontano2)>sigmamassima:
            sigmamassima=np.abs(sigmadelpuntopiulontano2)
    tresca1=((sigmadelpuntopiulontano1**2)+4*(tau**2))**0.5
    mises1=((sigmadelpuntopiulontano1**2)+3*(tau**2))**0.5
    tresca2=((sigmadelpuntopiulontano2**2)+4*(tau**2))**0.5
    mises2=((sigmadelpuntopiulontano2**2)+3*(tau**2))**0.5
    tresca=np.matrix(tresca1,tresca2)
    mises=np.matrix("0 0")
    tresca=np.matrix("0 0")
    mises[0,0]=mises1
    mises[0,1]=mises2
    tresca[0,0]=tresca1
    tresca[0,1]=tresca2
    #%if  sigmamassimadiprogetto>max(tresca,mises)
    #%fprintf('quella sezione resiste \n');
    #%elseif sigmamassimadiprogetto<max(tresca,mises)
    #%fprintf('quella sezione non resiste \n');
    #%end
    
    #%ricorda_gon=ricorda*200/pi;
    #%rettadelnullo_gon=rettadelnullo*200/pi;
    #%kappa=4;
    
    #%for i=1:11
    #%	for j=1:4
    #%	stampa(i,j)=arrotondadecimali(kappa,stampa(i,j));
    #%	end
    #%end
    
    #%cd risultati
    #%csvwrite('produzionesollecitazione.csv',stampa,0,0);
    #%csvwrite('ristampasollecitazione.csv',sollecitazione,0,0);
    #%cd ..
    
    #%disp('complimenti hai finito un intero programma!!!!!')
    #end
    return puntopiulontanoyyy1,puntopiulontanoxxx1,puntopiulontanoyyy2,puntopiulontanoxxx2,sigmadelpuntopiulontano1,sigmadelpuntopiulontano2,tresca,mises