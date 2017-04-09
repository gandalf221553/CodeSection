def xgeom(numero1,kk):
    printa=0
    from calcolatrice.misuras import size2
    import numpy as np
    numerodifiguregeneriche=size2(numero1,1)
    if printa:
        print("aaa",numerodifiguregeneriche)
    #print(numerodifiguregeneriche)
    #print(np.size(numero1,0))
    #print(np.size(numero1,1))
    vettore_baricentrix=np.zeros((numerodifiguregeneriche,1))
    vettore_baricentriy=np.zeros((numerodifiguregeneriche,1))
    vettore_centroix=np.zeros((numerodifiguregeneriche,1))
    vettore_centroiy=np.zeros((numerodifiguregeneriche,1))
    vettore_area=np.zeros((numerodifiguregeneriche,1))
    vet_m_inerzia=np.zeros((numerodifiguregeneriche,4))
    momenti_statici_totali=np.zeros((1,2))
    momenti_statici_totali_sm=np.zeros((1,2))
    momenti_statici_m=np.zeros((numerodifiguregeneriche,2))
    vettore_area_is=np.zeros((numerodifiguregeneriche,1))
    momenti_statici_is=np.zeros((numerodifiguregeneriche,2))
    vet_m_inerzia_is=np.zeros((numerodifiguregeneriche,4))
    matrice_huygens_totale=np.zeros((1,4))
    matrice_inerzia_is_totale=np.zeros((1,4))
    vettore_pesi_specifici=np.zeros((numerodifiguregeneriche,1))
    VetFigGen=range(0,numerodifiguregeneriche)
    if printa:
        print("aaa",vettore_area)
    from calcolatrice.studiatore2 import studianumero1
    from calcolatrice.misuras import EstraiUnaRiga, transponi
    for i in VetFigGen:
        calcolo=1

        ########################################
        #print("numero1zz")
        #print(numero1)
        #print(i)
        numero45=EstraiUnaRiga(numero1,i)
        #print("numero45",numero45)
        ########################################
        (coordinate,baricentrox,baricentroy,area,momenti_statici,matrice_inerzia,centroix,centroiy,numero42,peso_specifico)=studianumero1(numero45,kk,calcolo,0,0,0)
        vettore_pesi_specifici[i,0]=peso_specifico
        #%baricentrox
        vettore_baricentrix[i,0]=baricentrox
        #%baricentroy
        vettore_baricentriy[i,0]=baricentroy
        #%vettore delle aree
        vettore_area[i,0]=area
        #%centro di inerzia
        vettore_centroix[i,0]=centroix
        vettore_centroiy[i,0]=centroiy
        #%momenti_statici
        momenti_statici_m[i,0]=momenti_statici[0,0]
        momenti_statici_m[i,1]=momenti_statici[0,1]
        #%matrice_inerzia
        vet_m_inerzia[i,0]=matrice_inerzia[0,0]
        vet_m_inerzia[i,1]=matrice_inerzia[0,1]
        vet_m_inerzia[i,2]=matrice_inerzia[1,0]
        vet_m_inerzia[i,3]=matrice_inerzia[1,1]
        #print(vettore_pesi_specifici,vettore_area,vettore_baricentrix,vettore_baricentriy)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #print("ffffff",vettore_baricentrix,vettore_baricentriy)
    areatotale=0
    if printa:
        print("aaa",vettore_area)
    from calcolatrice.misuras import SommaDegliScalari
    for i in VetFigGen:
        vettore_area_is[i,0]=vettore_area[i,0]*vettore_pesi_specifici[i,0]
        #from misuras import EstraiUnaRiga
        #cicc2=EstraiUnaRiga(vet_m_inerzia,i)
        momenti_statici_is[i,0]=np.dot(momenti_statici_m[i,0],vettore_pesi_specifici[i,0])
        momenti_statici_is[i,1]=np.dot(momenti_statici_m[i,1],vettore_pesi_specifici[i,0])
        vet_m_inerzia_is[i,0]=np.dot(vet_m_inerzia[i,0],vettore_pesi_specifici[i,0])
        vet_m_inerzia_is[i,1]=np.dot(vet_m_inerzia[i,1],vettore_pesi_specifici[i,0])
        vet_m_inerzia_is[i,2]=np.dot(vet_m_inerzia[i,2],vettore_pesi_specifici[i,0])
        vet_m_inerzia_is[i,3]=np.dot(vet_m_inerzia[i,3],vettore_pesi_specifici[i,0])
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #%calcolodelbaricentrototale
        areatotale=SommaDegliScalari(vettore_area_is)
        if areatotale==0:
            return print("areatotale==0")
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #print(vettore_area_is)
    #print(vettore_baricentrix)
    #print(vettore_baricentriy)
    essey=np.dot(transponi(vettore_baricentrix),vettore_area_is)
    essex=np.dot(transponi(vettore_baricentriy),vettore_area_is)
    #print(vettore_area_is)
    baricentrototalex=np.dot(essey,1/areatotale)
    baricentrototaley=np.dot(essex,1/areatotale)

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%calcolo dei momenti statici totali
    for i in VetFigGen:
        #for i=1:numerodifiguregeneriche
        momenti_statici_totali[0,0]=momenti_statici_totali[0,0]+momenti_statici_is[i,0]
        momenti_statici_totali[0,1]=momenti_statici_totali[0,1]+momenti_statici_is[i,1]
        momenti_statici_totali_sm[0,0]=np.dot(transponi(vettore_baricentriy),vettore_area_is)
        momenti_statici_totali_sm[0,1]=np.dot(transponi(vettore_baricentrix),vettore_area_is)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #%huygens-steiner

    vet_m_inerzia_huygens=np.zeros((numerodifiguregeneriche,4))
    from calcolatrice.misuras import huygstein
    for i in VetFigGen:
        #%distanza  del baricentro locale da baricentro totale
        deltax=0
        deltay=0
        deltax=baricentrototalex-vettore_centroix[i,0]
        """
        print("deltax")
        print(baricentrototalex)
        print(vettore_centroix[i,0])
        print(deltax)
        print("deltay")
        print(baricentrototaley)
        print(vettore_centroiy[i,0])
        print(deltay)
        """
        deltay=baricentrototaley-vettore_centroiy[i,0]
        vet_m_inerzia_huygens[i,:]=huygstein(vettore_area_is[i,0],deltax,deltay)
        #%vet_m_inerzia_huygens(i,:)=vet_m_inerzia_huygens(i,:).*vettore_pesi_specifici(i)

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    for i in VetFigGen:
        matrice_huygens_totale[0,0]=matrice_huygens_totale[0,0]+vet_m_inerzia_huygens[i,0]
        matrice_huygens_totale[0,1]=matrice_huygens_totale[0,1]+vet_m_inerzia_huygens[i,1]
        matrice_huygens_totale[0,2]=matrice_huygens_totale[0,2]
        matrice_huygens_totale[0,3]=matrice_huygens_totale[0,3]+vet_m_inerzia_huygens[i,3]
        matrice_inerzia_is_totale[0,1]=matrice_inerzia_is_totale[0,0]+vet_m_inerzia_is[i,0]
        matrice_inerzia_is_totale[0,1]=matrice_inerzia_is_totale[0,1]+vet_m_inerzia_is[i,1]
        matrice_inerzia_is_totale[0,1]=matrice_inerzia_is_totale[0,1]
        matrice_inerzia_is_totale[0,1]=matrice_inerzia_is_totale[0,3]+vet_m_inerzia_is[i,3]
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    matrice_inerzia_finale=vet_m_inerzia_huygens+vet_m_inerzia_is
    #print(matrice_inerzia_finale)
    if numerodifiguregeneriche==1:
        matrice_inerzia_totale=matrice_inerzia_finale
    else:
        from calcolatrice.misuras import SommaInColonne
        matrice_inerzia_totale=SommaInColonne(matrice_inerzia_finale)
    #print(matrice_inerzia_totale)
    from calcolatrice.misuras import assiprincipaliinerzia
    (inerzianii,inerziaeee,angolo_rad,angolo_gon,parametroaa,parametrobb,casoinesame)=assiprincipaliinerzia(matrice_inerzia_totale)
    Aangolo_rad=angolo_rad
    if printa:
        print(angolo_rad)
    Aangolo_gon=angolo_gon
    from math import pi
    Aangolo_grad=Aangolo_rad*180/pi

    rhoeee=(inerziaeee/areatotale)
    rhonii=(inerzianii/areatotale)

    if printa:
        print("matrice inerzia totale",matrice_inerzia_totale)
    if 0:
        print("cacca")
        print(vettore_area_is)
        print(baricentrototalex)
        print(baricentrototaley)
        print(vettore_baricentrix)
        print(vettore_baricentriy)
        print(essex)
        print(essey)
        print(vet_m_inerzia_huygens)
        print(matrice_inerzia_totale)
        print(Aangolo_rad)
        print(Aangolo_gon)
        print(Aangolo_grad)
        print(rhoeee)
        print(rhonii)
        print(casoinesame)
        print(inerziaeee)
        print(inerzianii)
    
    return areatotale,baricentrototalex,baricentrototaley,essex,essey,\
    matrice_inerzia_totale,Aangolo_rad,Aangolo_gon,Aangolo_grad,angolo_rad,\
    rhoeee,rhonii,casoinesame,inerziaeee,inerzianii
    