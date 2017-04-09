def contorna(listadicoordinatefinale,numero1,kk,discretizzaarchicerchi):
    #function [contorni]=contornalacomposizione()
    aa=0 #%uguale a 1 se vuoi fare un controllo all'inizio e alla fine
    from math import floor, ceil
    from calcolatrice.misuras import size2,minimo,massimo,DentroLaFigura,RiduciDimensioni,UnireMatriciCol
    import numpy as np
    if aa:
        print(listadicoordinatefinale)
        print(size2(listadicoordinatefinale,0))
    #%listadicoordinatefinale=[[0 0 5 5 0 0 0 2 2 0];[0 5 5 0 0 0 2 2 0 0]]';
    #%numerodifiguregeneriche=1;
    numerodifiguregeneriche=size2(numero1,1) #% dimmi quante figure vuoi inserire
    #%definisci il passo del calcolo
    righe=size2(listadicoordinatefinale,1)
    passo=10
    Vet1=range(0,righe-1)
    for i in Vet1:
        Vet2=range(i+1,righe)
        for j in Vet2:
            distanza=((listadicoordinatefinale[i,0]-listadicoordinatefinale[j,0])**2+(listadicoordinatefinale[i,1]-listadicoordinatefinale[j,1])**2)**0.5
            #print(distanza)
            if distanza<passo and distanza>0:
                passo=distanza
    #%il numero può essere modulato liberamente tra 'passo/n' e 'passo'
    inpiu=2
    #%passo=0.25;
    xv=listadicoordinatefinale[:,0]
    yv=listadicoordinatefinale[:,1]
    xmin=floor(minimo(xv))-inpiu
    xmax=ceil(massimo(xv))+inpiu
    ymin=floor(minimo(yv))-inpiu
    ymax=ceil(massimo(yv))+inpiu
    
    #passo=np.minimum((xmax-xmin)/passo,(ymax-ymin)/passo)*2
    #print(xmin,xmax,ymin,ymax)
    #%arrotonda xmin inferiormente e poi sali di un tasso fisso fino a xmax arrotondato superiormente
    #%arrotonda xmin inferiormente e poi sali di un tasso fisso fino a xmax arrotondato superiormente
    if aa:
        print(xmin,xmax,ymin,ymax,ceil(passo))
    xa=np.linspace(xmin,xmax,ceil(passo),endpoint=True)
    ya=np.linspace(ymin,ymax,ceil(passo),endpoint=True)
    magliacx,magliacy=np.meshgrid(xa,ya)
    #print(size2(xa,1),size2(xa,2),size2(ya,1),size2(ya,2),size2(magliacx,1),size2(magliacx,2),size2(magliacy,1),size2(magliacy,2))
    from calcolatrice.studiatore2 import studianumero1
    VetNum=range(0,numerodifiguregeneriche)
    inlocale=np.asmatrix(np.zeros((size2(magliacx,1),size2(magliacx,2))))
    for i in VetNum:
        calcolo=4
        coordinate,b2,b3,b4,b5,b6,b7,b8,b9,peso_specifico=studianumero1(numero1[i,:],kk,calcolo,discretizzaarchicerchi,0,0)
        #[coordinate,~,~,~,~,~,~,~,~,peso_specifico]=studiatore(numero1(i,:),kk,calcolo,discretizzaarchicerchi,0,0);
        #%peso_specifico=1;
        #%coordinate=[[0 0 5 5 0];[0 5 5 0 0]]';
        if peso_specifico>0:
            coordx=coordinate[:,0]
            coordy=coordinate[:,1]
            dentro=DentroLaFigura(coordinate,magliacx,magliacy)
            inlocale=inlocale+dentro
            #%inlocale=inlocale+on; noto dei problemi con i contorni,
            #%capita che vengono contati due volte
    for i in VetNum:
        calcolo=4;
        coordinate,b2,b3,b4,b5,b6,b7,b8,b9,peso_specifico=studianumero1(numero1[i,:],kk,calcolo,discretizzaarchicerchi,0,0)
        #%peso_specifico=-1;
        #%coordinate=[[0 0 2 2 0];[0 2 2 0 0]]';
        if peso_specifico<0:
            coordx=coordinate[:,0]
            coordy=coordinate[:,1]
            innega=DentroLaFigura(coordinate,magliacx,magliacy)
            inlocale=inlocale-innega
    #inlocale=inlocale-onnega; noto dei problemi con i contorni,
    #capita che vengono contati due volte
    #print(inlocale)
    #np.savetxt("cacca.csv", inlocale, delimiter=' ', header='')
    #%clf;
    #%plot (coordx', coordy');
    #%hold on;
    magliacx,magliacy,inlocale=RiduciDimensioni(magliacx,magliacy,inlocale) 
    #size2(inlocale,0)
    numerodicontorni=0
    vetto=size2(listadicoordinatefinale,1)
    VetViz1=range(0,size2(inlocale,1))
    VetViz2=range(0,size2(inlocale,2))
    #print(vetto,VetViz1,VetViz2)
    VetK1=range(0,vetto)
    #print(size2(inlocale,1),size2(inlocale,2))
    vuota=np.matrix("0 0")
    vai=0
    for k in VetK1:
        centra=0
        coordx=listadicoordinatefinale[k,0]
        coordy=listadicoordinatefinale[k,1]
        for i in VetViz1:
            for j in VetViz2:
                #print(i,j)
                if inlocale[i,j]>0.5:
                    distanza=((coordx-magliacx[i,j])**2+(coordy-magliacy[i,j])**2)**0.5
                    if distanza<=2*passo:
                        centra=1
                        #i=size2(inlocale,1)
                        #j=size2(inlocale,2)
                        #%plot (magliacx(i,j), magliacy(i,j), "@g");
                        if vai==0:
                            vai=vai+1
                            contorni=np.matrix("0 0")
        if centra==1:
            contorni=UnireMatriciCol(contorni,vuota)
            contorni[numerodicontorni,0]=coordx
            contorni[numerodicontorni,1]=coordy
            numerodicontorni=numerodicontorni+1
    contorni=contorni[0:numerodicontorni-1,0:2]
                


    #%hold off;
    if aa:
        print(contorni)
        print(size2(contorni,0))
    return contorni
