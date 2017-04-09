# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 12:22:43 2017

@author: Von Braun
"""
def guardasecisonoaste(self):
    import numpy as np
    fugure=np.size(self.stringa,0)-1
    cisono=0
    VetR=range(1,fugure)
    for i in VetR:
        if self.vada==2.5:
            cisono=cisono+1
    if cisono>0:
        return 0
    else:
        return 1
    
def clear_all():
    """Clears all the variables from the workspace of the spyder application."""
    gl = globals().copy()
    for var in gl:
        if var[0] == '_': continue
        if 'func' in str(globals()[var]): continue
        if 'module' in str(globals()[var]): continue

        del globals()[var]
        
def size2(a,m):
    #import numpy as np
    import numpy as np
    b=0
    if m==2:
        b=np.size(a,1)
    elif m==1:
        b=np.size(a,0)
    else:
        print(np.size(a,0),np.size(a,1))
    return b

def transponi(matr):
    import numpy as np
    matr=np.transpose(matr)
    return matr
	
def CancellaUnaRiga(matr,riga):
    import numpy as np
    from misuras import size2
    righevecchie=size2(matr,1)
    colonnevecchie=size2(matr,2)
    nuova=np.zeros((righevecchie-1,colonnevecchie))
    VetRigheGen=range(0,righevecchie+1)
    VetCOlonGen=range(0,colonnevecchie+1)
    for i in VetRigheGen:
        for j in VetCOlonGen:
            if i<riga:
                nuova[i,j]=matr[i,j]
            elif i==riga:
                print("nada")
            else:
                nuova[i-1,j]=matr[i,j]
    return nuova
	
def EstraiUnaRiga(matr,riga):
    import numpy as np
    colonnevecchie=size2(matr,2)
    nuova=np.zeros((1,colonnevecchie))
    VetCOlonGen=range(0,colonnevecchie)
    """
    print("riga")
    print(riga)
    print(colonnevecchie)
    print(np.size(matr,1))
    print(np.size(matr,0))
    print(np.size(nuova,1))
    print(np.size(nuova,0))
    print("VetCOlonGen")
    print(np.size(VetCOlonGen,0))
    #print(VetCOlonGen)
    """
    for j in VetCOlonGen:
        #print(j)
        nuova[0,j]=matr[riga,j]
    return nuova

def EstraiUnaColonna(matr,colonna):
    import numpy as np
    righevecchie=size2(matr,1)
    nuova=np.zeros((righevecchie,1))
    VetRigheGen=range(0,righevecchie)
    for i in VetRigheGen:
        if i==colonna:
            nuova[i,0]=matr[i,colonna]
    return nuova
    
def EstraiUnPezzo(matr,rigai,rigaf,coloi,colof):
    import numpy as np
    #print(matr)
    righe=size2(matr,1)
    colonne=size2(matr,2)
    if rigaf=="end":
        righenuove=righe-rigai
    else:
        righenuove=rigaf-rigai
    if colof=="end":
        colonnenuove=colonne-coloi
    else:
        colonnenuove=colof-coloi
    #print(righenuove,colonnenuove)
    nuova=np.asmatrix(np.zeros((righenuove,colonnenuove)))
    VetRigheGen=range(0,righenuove)
    VetColonGen=range(0,colonnenuove)
    #print(VetColonGen,VetRigheGen)
    #print(VetColonGen,VetRigheGen,righenuove,colonnenuove)
    for i in VetRigheGen:
        for j in VetColonGen:
            #print(i+rigai,j+coloi)
            nuova[i,j]=matr[i+rigai,j+coloi]
    #print(nuova)
    return nuova
	
def zeros(righe, colonne):
    VetRigheGen=range(0,righe)
    VetColonGen=range(0,colonne)
    import numpy as np
    zeris=np.matrix(righe, colonne)
    for i in VetRigheGen:
        for j in VetColonGen:
            zeris[i,j]=0
    return zeris
	
def ProdVettoriale(a,b):
    import numpy as np
    if size2(a,1)==size2(b,2):
        VetRigheGen=range(0,size2(a,2))
        VetColonGen=range(0,size2(b,1))
        c=np.zeros(size2(a,2),size2(b,1))
        i=0
        j=0
        for i in VetRigheGen:
            c[i,j]=0
            for j in VetColonGen:
                c[i,j]=c[i,j]+a[i,j]*b[i,j]
            else:
                print("non è un risultato")
                c=0
    return c

def SommaDegliScalari(a):
    VetRigheGen=range(0,size2(a,1))
    VetColonGen=range(0,size2(a,2))
    b=0
    for i in VetRigheGen:
        for j in VetColonGen:
            b=b+a[i,j]
    return b

def SommaInColonne(matrice):
    VetRigheGen=range(0,size2(matrice,1))
    VetColonGen=range(0,size2(matrice,2))
    import numpy as np
    zeris=np.zeros((1, size2(matrice,2)))
    for j in VetColonGen:
        somma=0
        for i in VetRigheGen:
            somma=somma+matrice[i,j]
        zeris[0,j]=somma
    return zeris

def rigacnf(riga1,riga2):
    r1=size2(riga1,1)
    r2=size2(riga1,2)
    r3=size2(riga2,1)
    r4=size2(riga2,2)
    r5=SommaDegliScalari(riga1)
    r6=SommaDegliScalari(riga2)
    m=1
    dipende=0
    #print(r1,r2,r3,r4,r5,r6)
    if r1==r3 and r2==r4 and r5==r6:
        for i in range(0,r1):
            for j in range(0,r2):
                if riga1[i,j]!=riga2[i,j]:
                    m=m+1
        if m==1:
            dipende=1
    else:
        dipende=0
    return dipende

    
def StringCnf(riga1,riga2):
    r1=len(riga1)
    r2=len(riga2)
    dipende=0
    m=1
    #print(r1,r2,r3,r4,r5,r6)
    T1=range(0,r1)
    if r1==r2:
        for i in T1:
            #print(riga1[i],riga2[i])
            if riga1[i]!=riga2[i]:
                m=m+1
        if m==1:
            dipende=1
    else:
        dipende=0
    return dipende


def listare(numero1,kk,discretizzaarchicerchi):
    #%prendi una figura geometrica da un file dati
    #from misuras import size2,UnireMatriciCol
    from calcolatrice.studiatore2 import studianumero1
    import numpy as np
    numerodifiguregeneriche=size2(numero1,1) #% dimmi quante figure vuoi inserire
    #%vettore_spostamento=[0 0];
    #%listadicoordinate=zeros(1,4)
    VetRigheGen=range(0,numerodifiguregeneriche)
    #print(numero1)
    for i in VetRigheGen:
        calcolo=4
        ciro=np.asmatrix(numero1[i,:])
        #print("primadel4",ciro)
        #print(type(ciro))
        coordinate,b1,b2,b3,b4,b5,b6,b7,b8,peso_specifico=studianumero1(ciro,kk,calcolo,discretizzaarchicerchi,0,0);
        #print("cazzu cazzu",coordinate)
        #mi servono solo le variablili "coordinate" e "peso:specifico"
        coordinate=np.asmatrix(coordinate)
        #print("dopoil4",coordinate)
        if i==0:
            listadicoordinate=coordinate
            listadicoordinate=np.asmatrix(listadicoordinate)
            #print("nell'uno",listadicoordinate)
        else:
            listadicoordinate=UnireMatriciCol(listadicoordinate,coordinate)
            #print("neidopo",listadicoordinate)
            listadicoordinate=np.asmatrix(listadicoordinate)

    return listadicoordinate
    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %coppie che vanno tenute per forza assolutamente!!!!! da fare anche per gli altri disegni	
    %listadicoordinate(numerodirimaste,1)=xdarototraslare;
    %listadicoordinate(numerodirimaste,2)=ydarototraslare;				
    %numerodirimaste=numerodirimaste+1;
    %xdarototraslare=raggioesterno*cos(angolof);
    %ydarototraslare=raggioesterno*sin(angolof);
    %listadicoordinate(numerodirimaste,1)=xdarototraslare;
    %numerodirimaste=numerodirimaste+1;
    """
    
def CancDoppioni(a):
    #from misuras import size2, rigacnf,UnireMatriciCol
    import numpy as np
    #print(a,size2(a,1),size2(a,2))
    a=np.asmatrix(a)
    punti=size2(a,1)
    b=np.asmatrix(a[0,:])
    VetPunti=range(1,punti) #deve partire dalla seconda riga
    VetCol=range(0,2)
    #print(punti,b,VetPunti,VetCol)
    #print(VetCol)
    for i in VetPunti:
        kk=7
        VetCol=range(0,size2(b,1))
        #print(VetCol)
        #print(b)
        #print(a[i,:])
        #☺print(VetCol)
        for j in VetCol:
            r1=np.asmatrix(b[j,:])
            r2=np.asmatrix(a[i,:])
            ee=rigacnf(r1,r2)
            #print(ee)
            kk=kk+ee
            #print(i,j,ee)
            #print(b)
            #print(r1,r2,ee)
        #print("kk",kk,a[i,:])
        if kk==7:
            k=a[i,:]
            k=np.asmatrix(k)
            #print("a",np.size(a,0),np.size(a,1))
            #print("k",np.size(k,0),np.size(k,1))
            b=UnireMatriciCol(b,k)
    # print(b)
    
    #print(b,size2(b,1),size2(b,2))

    return b
    """
    %prendo la prima riga e la metto nelle righe valutate
    %guardo ogni riga (la prima non la devo neanche guardare, in fin dei conti non la devo mica copiare
    %la confronto singolarmente con ogni altra
    %ee dice se le righe sono uguali (se sono tutte composte da uno allora sono la somma di tutti gli elementi è uguale a 
    %se due righe sono uguali, allora kk viene incrementato
    %confrontando ognuna delle righe di b con la a, se nessuna ottiene 1 vuol dire che va inserita nella b
    %se kk viene incrementato vuol dire che la riga è doppia allora non viene copiata nella nuova matrice
    %se la riga non è doppia (kk rimane costante) allora viene copiata nella nuova matrice se non è doppia, cioè viene incrementata,
    
    %funzione confronta una ad una le righe e copia una volta, se ci sono doppioni non li ricopia
    %se uno vuole confrontare le colonne, può anche trasporre la matrice
    %se uno vuole confrontare solo una parte di una matrice, in 
    """
    
def UnireMatriciColNon(a,b):
    import numpy as np
    r1=size2(a,1)
    r2=size2(a,2)
    r3=size2(b,1)
    r4=size2(b,2)
    a=np.asmatrix(a)
    b=np.asmatrix(b)
    #if asse==0.:
    rmax=r2
    if r4>r2:
        rmax=r4
    #if r2!=r4:
        #return 0
    culo=np.matrix(np.zeros((r1+r3,rmax)))
    righe=range(0,r1)
    srighe=range(r1,r3+r1)
    colonne=range(0,r2)
    scolonne=range(0,r4)
    #print(righe,colonne,srighe,scolonne)
    for i in righe:
        for j in colonne:
            #print(i,j, a[i,j])
            culo.itemset((i,j),a.item((i,j)))
    for i in srighe:
        for k in scolonne:
            #print(i,k, b[i-r1,k])
            culo.itemset((i,k),b.item((i-r1,k)))
    return culo
def UnireMatriciCol(a,b):
    import numpy as np
    r1=size2(a,1)
    r2=size2(a,2)
    r3=size2(b,1)
    r4=size2(b,2)
    a=np.asmatrix(a)
    b=np.asmatrix(b)
    #if asse==0.:
    if r2!=r4:
        return 0
    culo=np.matrix(np.zeros((r1+r3,r2)))
    righe=range(0,r1)
    srighe=range(r1,r3+r1)
    colonne=range(0,r2)
    scolonne=range(0,r4)
    #print(righe,colonne,srighe,scolonne)
    for i in righe:
        for j in colonne:
            #print(i,j, a[i,j])
            culo.itemset((i,j),a.item((i,j)))
    for i in srighe:
        for k in scolonne:
            #print(i,k, b[i-r1,k])
            culo.itemset((i,k),b.item((i-r1,k)))
    return culo
def UnireMatriciRigNon(a,b):
    import numpy as np
    r1=size2(a,1)
    r2=size2(a,2)
    r3=size2(b,1)
    r4=size2(b,2)
    a=np.asmatrix(a)
    b=np.asmatrix(b)
    #if asse==0.:
    #if r1!=r3:
        #return 0
    rmax=r1
    if r3>r1:
        rmax=r3
    culo=np.matrix(np.zeros((rmax,r2+r4)))
    righe=range(0,r1)
    srighe=range(0,r3)
    colonne=range(0,r2)
    scolonne=range(r2,r2+r4)
    #print(righe,colonne,srighe,scolonne)
    for i in righe:
        for j in colonne:
            #print(i,j, a[i,j])
            culo.itemset((i,j),a.item((i,j)))
    for i in srighe:
        for k in scolonne:
            #print(i,k, b[i,k-r2])
            culo.itemset((i,k),b.item((i,k-r2)))
    return culo    
def UnireMatriciRig(a,b):
    import numpy as np
    r1=size2(a,1)
    r2=size2(a,2)
    r3=size2(b,1)
    r4=size2(b,2)
    a=np.asmatrix(a)
    b=np.asmatrix(b)
    #if asse==0.:
    if r1!=r3:
        return 0
    culo=np.matrix(np.zeros((r1,r2+r4)))
    righe=range(0,r1)
    srighe=range(0,r3)
    colonne=range(0,r2)
    scolonne=range(r2,r2+r4)
    #print(righe,colonne,srighe,scolonne)
    for i in righe:
        for j in colonne:
            #print(i,j, a[i,j])
            culo.itemset((i,j),a.item((i,j)))
    for i in srighe:
        for k in scolonne:
            #print(i,k, b[i,k-r2])
            culo.itemset((i,k),b.item((i,k-r2)))
    return culo    

    
def rototrasl(xdarototraslare,ydarototraslare,dex,dey,angolo_rad,moltiplica):
    from math import cos, sin
    xdarototraslare=xdarototraslare-dex
    ydarototraslare=ydarototraslare-dey
    if moltiplica=="1":
        xrototraslato=0
        yrototraslato=float(moltiplica)*(-xdarototraslare*sin(angolo_rad)+ydarototraslare*cos(angolo_rad))
    else:
        xrototraslato=moltiplica*(xdarototraslare*cos(angolo_rad)+ydarototraslare*sin(angolo_rad))
        yrototraslato=moltiplica*(-xdarototraslare*sin(angolo_rad)+ydarototraslare*cos(angolo_rad))

    #%angolo_rad*180/pi;
    return xrototraslato,yrototraslato
    
def angolopolarecartesiano(deltax,deltay):
    from math import atan2, pi
    theta=atan2(deltay,deltax)
    if (theta<0):
        theta=2*pi+theta
    return theta


def assiprincipaliinerzia(matriceinerzia):
    #print(matriceinerzia)
    inerziay=0
    inerziax=0
    inerziaxy=0
    inerziay=matriceinerzia[0,0]
    inerziaxy=matriceinerzia[0,1]
    inerziax=matriceinerzia[0,3]
    kappa=6
    inerziay=round(inerziay,kappa)
    inerziax=round(inerziax,kappa)
    inerziaxy=round(inerziaxy,kappa)
    casoinesame=0
    from math import pi
    if inerziaxy==0:
        angolo_rad=0
    elif inerziay==inerziax:
        if inerziaxy>0:
            angolo_rad=pi/4
        else:
            angolo_rad=-pi/4
    else:
        from math import atan
        angolo_rad=0.5*atan((2*inerziaxy)/(inerziay-inerziax))
    angolo_gon=angolo_rad*200/pi
    parametroaa=(inerziax+inerziay)/2
    parametrobb=(0.5*(((inerziax-inerziay)**2)+4*(inerziaxy)**2)**0.5)


    if inerziax>inerziay:
        casoinesame=11
        inerziaeee=parametroaa+parametrobb
        inerzianii=parametroaa-parametrobb
    elif inerziax<inerziay:
        casoinesame=15
        inerziaeee=parametroaa-parametrobb
        inerzianii=parametroaa+parametrobb
    else:
        casoinesame=19
        inerziaeee=parametroaa+parametrobb
        inerzianii=parametroaa-parametrobb
            
    #print(angolo_rad,parametroaa,parametrobb,inerziaeee,inerzianii)
    return inerzianii,inerziaeee,angolo_rad,angolo_gon,parametroaa,parametrobb,casoinesame

"""
import numpy as np
matriceinerzia=np.matrix('1 2 3')
print(matriceinerzia)
(inerzianii,inerziaeee,angolo_rad,angolo_gon,parametroaa,parametrobb,casoinesame)=assiprincipaliinerzia(matriceinerzia)
print(inerziaeee)
"""

def huygstein(area,deltax,deltay):
    """#%huygens-steiner
    print(area)
    print(deltax)
    print(deltay)"""
    import numpy as np
    huygens=np.zeros((1, 4))
    huygens[0,0]=area*(deltax**2)
    huygens[0,1]=area*(deltax*deltay)
    huygens[0,2]=huygens[0,1]
    huygens[0,3]=area*(deltay**2)
    """"print(3333333333)
    print(huygens)"""
    return huygens
    
    
def RotatInerz(inerzia_ix,inerzia_iy,inerzia_ixy,rotazione_rad):
    from math import sin, cos
    a=inerzia_ix;
    b=inerzia_iy;
    c=inerzia_ixy;
    inerzia_lungox=a*((cos(rotazione_rad))**2)+b*((sin(rotazione_rad))**2)-2*c*sin(rotazione_rad)*cos(rotazione_rad)
    inerzia_lungoy=a*((sin(rotazione_rad))**2)+b*((cos(rotazione_rad))**2)+2*c*sin(rotazione_rad)*cos(rotazione_rad)
    inerzia_lungoxy=0.5*(a-b)*sin(rotazione_rad)*cos(rotazione_rad)+c*(((cos(rotazione_rad))**2)-((sin(rotazione_rad))**2))
    return inerzia_lungox,inerzia_lungoy,inerzia_lungoxy

def arrotonda(a,kappa):
    import numpy as np
    r1=size2(a,1)
    r2=size2(a,2)
    b=np.asmatrix(np.zeros((r1,r2)))
    VetR1=range(0,r1)
    VetR2=range(0,r2)
    for i in VetR1:
        for j in VetR2:
            b[i,j]=round(a[i,j],kappa)
    return b

def minimo(a):
    import numpy as np
    a=np.asmatrix(a)
    r1=size2(a,1)
    r2=size2(a,2)
    b=a[0,0]
    VetR1=range(0,r1)
    VetR2=range(0,r2)
    for i in VetR1:
        for j in VetR2:
            if b>a[i,j]:
                b=a[i,j]
    return b
    
    
def massimo(a):
    import numpy as np
    a=np.asmatrix(a)
    r1=size2(a,1)
    r2=size2(a,2)
    b=a[0,0]
    VetR1=range(0,r1)
    VetR2=range(0,r2)
    for i in VetR1:
        for j in VetR2:
            if b<a[i,j]:
                b=a[i,j]
    return b
def ScalarXMatr(b,a):
    import numpy as np
    r1=size2(a,1)
    r2=size2(a,2)
    c=np.asmatrix(np.zeros((r1,r2)))
    VetR1=range(0,r1)
    VetR2=range(0,r2)
    for i in VetR1:
        for j in VetR2:
                c[i,j]=a[i,j]*b
    return c

    
    
def DentroLaFigura(x,magliax,magliay):
    import numpy as np
    from matplotlib import path
    """
    xv =transponi(np.matrix("0.05840, 0.48375, 0.69356, 1.47478, 1.32158,1.94545, 2.16477, 1.87639, 1.18218, 0.27615,0.05840"))
    yv =transponi(np.matrix("0.60628, 0.04728, 0.50000, 0.50000, 0.02015, 0.18161, 0.78850, 1.13589, 1.33781, 1.04650, 0.60628"))
    x=UnireMatriciRig(xv,yv)
    IsPointInside=np.matrix([[1,2],[1,9]])
    """
    #print("cacacacac",size2(magliax,0))
    IsPointInside=np.matrix("0 0")
    VetRig=size2(magliax,1)
    VetCol=size2(magliax,2)
    magliaz=np.asmatrix(np.zeros((VetRig,VetCol)))
    for i in range(VetRig):
        for j in range(VetCol):
            IsPointInside[0,0]=magliax[i,j]
            IsPointInside[0,1]=magliay[i,j]
            p = path.Path((x))
            aha=p.contains_points(IsPointInside)
            #print(aha)
            #print(IsPointInside)
            aha=np.asmatrix(aha)
            if aha:
                magliaz[i,j]=1
    #}print(size2(magliaz,0))
    return magliaz
"""
           VetH=range(0,size2(IsPointInside,1))
            k=0
            for i in VetH:
                if aha[0,i]:
                    if k==0:
                        new=IsPointInside[i,:]
                    else:
                        new=UnireMatriciRig(new,IsPointInside[i,:])
"""

def RiduciDimensioni(magliacx,magliacy,inlocale):
    somma=SommaDegliScalari(inlocale)
    r1=0
    r2=size2(inlocale,1)-1
    r3=0
    r4=size2(inlocale,2)-1
    somma1=somma
    while somma1==somma:
        r1=r1+2
        taron=inlocale[r1:r2,r3:r4]
        somma1=SommaDegliScalari(taron)    
    r1=r1-2
    somma1=somma
    while somma1==somma:
        r2=r2-2
        taron=inlocale[r1:r2,r3:r4]
        somma1=SommaDegliScalari(taron)    
    r2=r2+2
    somma1=somma
    while somma1==somma:
        r3=r3+2
        taron=inlocale[r1:r2,r3:r4]
        somma1=SommaDegliScalari(taron)    
    r3=r3-2
    somma1=somma
    while somma1==somma:
        r4=r4-2
        taron=inlocale[r1:r2,r3:r4]
        somma1=SommaDegliScalari(taron)    
    r4=r4+2
    magliacx=magliacx[r1:r2,r3:r4]
    magliacy=magliacy[r1:r2,r3:r4]
    inlocale=inlocale[r1:r2,r3:r4]
    #print(r1,r2,r3,r4)
    return magliacx,magliacy,inlocale
    
def FindCharInAString(Stringa, Carattere):
  Indice = 0
  while Indice<len(Stringa):
    if Stringa[Indice] == Carattere:
      return Indice
    Indice = Indice + 1
  return -1     

  
def StringaToMatrix(a):
    printa=0
    a=a.replace("\n","")
    a=a.replace("  "," ")
    a=a.replace("   "," ")
    if a[-1]==";":
        a=a[0:len(a)-1]
    if a[-1]==" ":
        a=a[0:len(a)-1]
    aSplit = a.split(';')
    #print(len(aSplit))
    if printa:
        print("aasdafafe",a)
    #print(aSplit[1])
    import numpy as np
    l = []
    colonnamassima=0
    #print(aSplit)
    for item in aSplit:
        subl = []
        subcols = []
        colonna=0
        for num in item.split(' '):
            colonna=colonna+1
            if printa:
                print(float(num))
            subl.append(num)
        subcols.append(colonna)
        colonnamassima=max(colonnamassima,colonna)
        l.append(subl)
        #print("subcols",subcols)
    matricefinale=np.asmatrix(np.zeros((1,colonnamassima)))
    inizia=0
    #print(matricefinale)
    #print(aSplit)
    primar=0
    if printa:
        print(aSplit)
    for item in aSplit:
        subl = []
        colonna=0
        #riga=np.matrix("0")
        riga=np.asmatrix(np.zeros((1,colonnamassima)))
        for num in item.split(' '):
            if printa:
                print(item.split(" "))
                print(num)
            if num==" " or num=="":
                riga[0,colonna-1]=0
            else:
                colonna=colonna+1
                #print(colonna)
                #print(num)
                if printa:
                    print(float(num))
                riga[0,colonna-1]=float(num)
                #subl.append(num)
        if printa:
            print("minteressa",riga)#=np.asmatrix(subl)
        
        
        primar=primar+1
        numer=np.size(riga,1)
        if primar==1:
            rigapiena=riga
        else:
            zeri=np.asmatrix(np.zeros((1,colonnamassima-numer)))
            rigapiena=UnireMatriciRig(riga,zeri)
        if printa:            
            print(rigapiena)
            print(np.size(rigapiena,0),np.size(rigapiena,1))
        inizia=inizia+1
        if inizia==1:
            matricefinale=rigapiena
        else:
            matricefinale=UnireMatriciCol(matricefinale,rigapiena)
    if printa:
        print(matricefinale)
        matricefinale=np.asmatrix(matricefinale)
    return matricefinale
    
    