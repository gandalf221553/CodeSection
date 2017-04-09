def studianumero1(numero1,kk,calcolo,discretizzaarchicerchi,traslax,traslay):
    from calcolatrice.misuras import size2, transponi,UnireMatriciRig,UnireMatriciCol,EstraiUnPezzo,ScalarXMatr
    #print("numero1 333", numero1)
    #print(size2(numero1,1))
    #print(size2(numero1,2))
    printa=0
    enne=6
	#il numero 1 è per: calcolare la geometria delle aree
	#il numero 2 è per: calcolare i minimi
	#il numero 3 è per: traslare tutto
	#il numero 4 è per: i contorni
	#il numero 5 è per: disegnare
    from math import floor,pi,cos,sin
    kk=floor(kk)
    import numpy as np
    coordinate=np.matrix("0 0")
    baricentrox=0
    baricentroy=0
    area=0
    momenti_statici=np.matrix("0 0")
    matrice_inerzia=np.matrix("0 0; 0 0")
    centroix=0
    centroiy=0
    peso_specifico=0
    #siamo nel python quindi non è più i=1 ma i=0
    i=0
    #print("ddasdas",numero1)
    peso_specifico=numero1[0,1]
    if numero1[i,0]==1.:
        if printa:
            print(numero1)
    #%studio della riga del csv
    #%per il cerchio
    #%circle 	(X Center,Y Center,Radius)
        coordxc=numero1[i,kk+0]
        coordyc=numero1[i,kk+1]
        raggio=numero1[i,kk+2]
        if calcolo==1:
            area=pi*(raggio**2)
            momenti_statici=np.matrix("0 0")
            baricentrox=coordxc
            baricentroy=coordyc
            centroix=coordxc
            centroiy=coordyc
            inerz=pi*(raggio**4)*0.25
            matrice_inerzia=np.matrix(np.zeros((2,2)))
            matrice_inerzia[0,0]=matrice_inerzia[1,1]=inerz
        elif calcolo==2:
            centroix=numero1[i,kk+0]-raggio
            centroiy=numero1[i,kk+1]-raggio
        elif calcolo==3:
            numero1[i,kk+0]=numero1[i,kk+0]+traslax
            numero1[i,kk+1]=numero1[i,kk+1]+traslay
        elif calcolo==4 or calcolo==5:
            if calcolo==4:
                discretizzaarchicerchi=floor(discretizzaarchicerchi/enne)
            #ago=np.linspace(0,2*pi,discretizzaarchicerchi+1)
            #%angoloi=0; angolof=2*pi;
            ago=np.asmatrix(np.linspace(0,2*pi,discretizzaarchicerchi+1))
            c=transponi(np.asmatrix(np.add(coordxc,ScalarXMatr(raggio,np.cos(ago)))))
            d=transponi(np.asmatrix(np.add(coordyc,ScalarXMatr(raggio,np.sin(ago)))))
            discretizzaarchicerchi=floor(discretizzaarchicerchi)
            coordinate=UnireMatriciRig(c,d)
            #print(coordinate)
            #print(numero1)     
    #%arco di cerchio
    #%arc		(X Center,Y Center,Radius,Start angle,End angle)
    elif numero1[i,0]==2.:
        coordxc=numero1[i,kk+0]
        coordyc=numero1[i,kk+1]
        raggio=numero1[i,kk+2]
        angoloi=numero1[i,kk+3]
        angolof=numero1[i,kk+4]
        #print("ciccione",calcolo,coordxc,coordyc,raggio,angoloi,angolof)
        if calcolo==1:
            from calcolatrice.inerziasettorecoronacircolare import InerSettCoronCir
            baricentrox,baricentroy,area,momenti_statici,matrice_inerzia=InerSettCoronCir(raggio,angolof,angoloi,coordxc,coordyc)
            centroix=baricentrox
            centroiy=baricentroy
            #print(baricentrox,baricentroy,area,momenti_statici,matrice_inerzia)
        elif calcolo==2:
            centroix=numero1[i,kk+0]-raggio
            centroiy=numero1[i,kk+1]-raggio
        elif calcolo==3:
            #print("aaa")
            numero1[i,kk+0]=numero1[i,kk+0]+traslax
            numero1[i,kk+1]=numero1[i,kk+1]+traslay
        elif calcolo==4  or calcolo==5:
            if calcolo==4:
                discretizzaarchicerchi=floor(discretizzaarchicerchi/enne)
            discretoarco=floor(1+discretizzaarchicerchi*np.abs(angolof-angoloi)/(2*pi))
            ago=np.asmatrix(np.linspace(angoloi,angolof,discretoarco+1))
            c=transponi(np.asmatrix(np.add(coordxc,ScalarXMatr(raggio,np.cos(ago)))))
            d=transponi(np.asmatrix(np.add(coordyc,ScalarXMatr(raggio,np.sin(ago)))))
            discretoarco=floor(discretoarco)
            VetColonGen=range(1,discretoarco+1)
            c1=np.matrix(coordxc)
            c2=np.matrix(coordyc)
            d1=UnireMatriciCol(c1,c)
            d2=UnireMatriciCol(c2,d)
            coordinatex=UnireMatriciCol(d1,c1)
            coordinatey=UnireMatriciCol(d2,c2)
            coordinate=UnireMatriciRig(coordinatex,coordinatey)
            #print("cc",coordinate)


    elif numero1[i,0]==2.5:
        #print("evviva")
        coordx1=numero1[i,kk+0]
        coordy1=numero1[i,kk+1]
        coordx2=numero1[i,kk+2]
        coordy2=numero1[i,kk+3]
        spessore=numero1[i,kk+4]
        if calcolo==1:
            lunghezza=((coordx1-coordx2)**2+(coordy1-coordy2)**2)**0.5
            area=spessore*lunghezza
            baricentrox=(coordx1+coordx2)/2
            baricentroy=(coordy1+coordy2)/2
            centroix=baricentrox
            centroiy=baricentroy
            momentostatx=area*baricentroy
            momentostaty=area*baricentrox
            momenti_statici=np.asmatrix(np.zeros((1,2)))
            momenti_statici[0,0]=momentostatx
            momenti_statici[0,1]=momentostaty
            from math import atan2
            angolo=atan2(coordy1-coordy2,coordx1-coordx2)
            inerziax=spessore*(lunghezza**3)/12*(sin(angolo))**2
            inerziay=spessore*(lunghezza**3)/12*(cos(angolo))**2
            inerziaxy=spessore*(lunghezza**3)*cos(angolo)*cos(angolo)/12
            matrice_inerzia=np.asmatrix(np.zeros((2,2)))
            matrice_inerzia[0,0]=inerziay
            matrice_inerzia[0,1]=inerziaxy
            matrice_inerzia[1,0]=matrice_inerzia[0,1]
            matrice_inerzia[1,1]=inerziax
            #print(lunghezza,area,baricentrox,baricentroy,momenti_statici,matrice_inerzia)
        elif calcolo==2:
            centroix=np.minimum(numero1[i,kk+0],numero1[i,kk+0])
            centroiy=np.minimum(numero1[i,kk+1],numero1[i,kk+1])
        elif calcolo==3:
            numero1[i,kk+0]=numero1[i,kk+0]+traslax
            numero1[i,kk+1]=numero1[i,kk+1]+traslay
            numero1[i,kk+2]=numero1[i,kk+2]+traslax
            numero1[i,kk+3]=numero1[i,kk+3]+traslay
            #print(numero1)
        elif calcolo==4:
            coordinate=np.asmatrix(np.zeros((2,2)))
            coordinate[0,0]=coordx1
            coordinate[0,1]=coordy1
            coordinate[1,0]=coordx2
            coordinate[1,1]=coordy2
            #print(coordinate)
        elif calcolo==5:
            s=spessore
            if coordy1-coordy2==0:
                coordinate=np.asmatrix(np.zeros((5,2)))
                coordinate[0,0]=coordx1
                coordinate[1,0]=coordx1
                coordinate[2,0]=coordx2
                coordinate[3,0]=coordx2
                coordinate[4,0]=coordx1
                coordinate[0,1]=coordy1-s/2
                coordinate[1,1]=coordy1+s/2
                coordinate[2,1]=coordy2+s/2
                coordinate[3,1]=coordy2-s/2
                coordinate[4,1]=coordy1-s/2
            elif coordx1-coordx2==0:
                coordinate=np.asmatrix(np.zeros((5,2)))
                coordinate[0,0]=coordx1-s/2
                coordinate[1,0]=coordx1+s/2
                coordinate[2,0]=coordx2+s/2
                coordinate[3,0]=coordx2-s/2
                coordinate[4,0]=coordx1-s/2
                coordinate[0,1]=coordy1
                coordinate[1,1]=coordy1
                coordinate[2,1]=coordy2
                coordinate[3,1]=coordy2
                coordinate[4,1]=coordy1
            #print(coordinate)
    
    elif numero1[i,0]>=3.:
        #print("bravissimo")
        #print("numero1 5",numero1)
        punti=floor(numero1[i,0])
        #print("numero1",numero1)
        #print(punti)
        #%dovremmo guardare la polilinea nel senso opposto
        # from misuras import EstraiUnPezzo
        #numero2=numero1(1,kk+1:kk+((punti)*2))
        #numero2=EstraiUnPezzo(numero1,0,0,kk+1-1,kk-1+(punti)*2)
        pizza2=size2(numero1,2)+2
        pizza=np.asmatrix(np.zeros((1,pizza2)))
        #print("pizza",pizza)
        #zeros((1,))
        #print(numero1)
        if printa:
            print(np.size(numero1),kk,punti)
        pizza=np.asmatrix(numero1[:,kk:kk+(punti)*2])
        #pizza=np.asmatrix(EstraiUnPezzo(numero1,0,"end",kk,kk+(punti)*2))
        pizzavecchia=np.asmatrix(EstraiUnPezzo(numero1,0,"end",0,kk))
        #print("pv",size2(pizzavecchia,1),size2(pizzavecchia,2))
        #print(pizza)
        g=np.asmatrix("0 0")
        g[0,0]=pizza[0,0]
        g[0,1]=pizza[0,1]
        numero2=UnireMatriciRig(pizza,g)
        #print("pizza dopo", numero2)
        VetColonGen=range(0,punti)
        #print(VetColonGen)
        #print("numero22",numero2)
        if calcolo==1:
            area=0
            inerziax=0
            inerziay=0
            inerziaxy=0
            momentostatx=0
            momentostaty=0
            for k in VetColonGen:
                xi=numero2[i,2*k+0]
                yi=numero2[i,2*k+1]
                xip1=numero2[i,2*k+2]
                yip1=numero2[i,2*k+3]
                #print("pip", k, 2*k,2*k+1,2*k+2,2*k+3)
                #print("pip", k, xi,yi,xip1,yip1)

                #print(xi,yi,xip1,yip1)
                if xip1-xi==0.:
                    m=99999999999
                else:
                    m=(yip1-yi)/(xip1-xi)
                q=yi-m*xi
                area=area+(xip1**2-xi**2)*(m/2)+q*(xip1-xi)
                momentostatx=momentostatx+(xip1**3-xi**3)*((m**2)/6)+(xip1**2-xi**2)*(q*m/2)+(xip1-xi)*((q**2)/2)
                momentostaty=momentostaty+(xip1**3-xi**3)*(m/3)+(xip1**2-xi**2)*(q/2)
                inerziax=inerziax+(xip1**4-xi**4)*((m**3)/12)+(xip1**3-xi**3)*((q*m**2)/3)+(xip1**2-xi**2)*((q**2)*m/2)+(xip1-xi)*((q**3)/3)
                inerziay=inerziay+(xip1**4-xi**4)*(m/4)+(xip1**3-xi**3)*(q/3)
                inerziaxy=inerziaxy+(xip1**4-xi**4)*((m**2)/8)+(xip1**3-xi**3)*(q*m/3)+(xip1**2-xi**2)*((q**2)/4)
                #print("area",area,"barix",baricentrox,"bariy",baricentroy)
            if area<0:
                area=-area
                momentostatx=-(momentostatx)
                momentostaty=-(momentostaty)
                inerziax=-(inerziax)
                inerziay=-(inerziay)
                inerziaxy=-(inerziaxy)
            baricentrox=momentostaty/area
            baricentroy=momentostatx/area
            centroix=baricentrox
            centroiy=baricentroy
            momenti_statici=np.zeros((1,2))
            momenti_statici[0,0]=momentostatx
            momenti_statici[0,1]=momentostaty
            matrice_inerzia=np.zeros((2,2))
            matrice_inerzia[0,0]=inerziay-area*(baricentrox**2)
            matrice_inerzia[0,1]=inerziaxy-area*(baricentrox*baricentroy)
            matrice_inerzia[1,0]=matrice_inerzia[0,1]
            matrice_inerzia[1,1]=inerziax-area*(baricentroy**2)
        elif calcolo==2:
            centroix=numero2[i,0]
            centroiy=numero2[i,1]
            #print(centroix,centroiy)
            for k in VetColonGen:
                #print(numero2[i,2*k],numero2[i,2*k+1],centroix,centroiy)
                centroix=np.minimum(numero2[i,2*k+0],centroix)
                centroiy=np.minimum(numero2[i,2*k+1],centroiy)
        elif calcolo==3:
            #print(numero2)
            for k in VetColonGen:
                #print("bee",i,kk+2*k+1-1+1,kk+2*k+1-1+2)
                numero2[i,2*k+0]=numero2[i,2*k+0]+traslax
                numero2[i,2*k+1]=numero2[i,2*k+1]+traslay
            pizzafinale=np.matrix(np.zeros((1,size2(numero1,2)-kk-2*k-2)))
            numero1=UnireMatriciRig(pizzavecchia,numero2[:,0:-2])
            numero1=UnireMatriciRig(numero1,pizzafinale)
            #print(numero1)
        elif calcolo==4 or calcolo==5:
            #print(numero2)
            coordinate=np.asmatrix(np.zeros((punti+1,2)))
            #print(coordinate)
            #print("ad",numero2)
            #print(coordinate,VetColonGen,numero2)
            for k in VetColonGen:
                coordinate[k,0]=numero2[i,2*k+0]
                coordinate[k,1]=numero2[i,2*k+1]
            coordinate[k+1,0]=numero2[i,0]
            coordinate[k+1,1]=numero2[i,1]
            #print(coordinate)
                #print(coordinate)

    

    """
    print("nbaricentri")
    print(coordinate)
    print(baricentrox)
    print(baricentroy)
    print(area)
    print(momenti_statici)
    print(matrice_inerzia)
    print(centroix)
    print(centroiy)
    print(numero1)
    print(peso_specifico)
    """
    coordinate=np.asmatrix(coordinate)
    return coordinate,baricentrox,baricentroy,area,momenti_statici,matrice_inerzia,centroix,centroiy,numero1,peso_specifico

			