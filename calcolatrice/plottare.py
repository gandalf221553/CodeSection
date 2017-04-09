def poltrire(self,numero1,kk,discretizzaarchicerchi,vuoifareancheilnocciolo\
             ,noccioloordinato,listadicoordinatefinale,traslax,traslay,\
             sollecitazione,baricentrototalex,baricentrototaley,Aangolo_rad,\
             rhonii,rhoeee,puntopiulontanoyyy1,puntopiulontanoxxx1,\
             puntopiulontanoyyy2,puntopiulontanoxxx2,sigmadelpuntopiulontano1,\
             sigmadelpuntopiulontano2,angolo_rad):
    #print(numero1)
    #print(listadicoordinatefinale)
    #function poltrire(numero1,kk,nomArch,discretizzaarchicerchi,vuoifareancheilnocciolo,noccioloordinato,listadicoordinatefinale,traslax,traslay,sollecitazione,x)
    vuoiplottare=1
    scherza=0
    printa=0
    #%x.Aangolo_rad %quello dellasse neutro
    #%x.angolo_rad %quello della solleciazione
    import numpy as np
    from math import pi, cos, sin
    from calcolatrice.misuras import size2,minimo,massimo
    numerodifiguregeneriche=size2(numero1,1) # % dimmi quante figure vuoi inserire
    VetFig=range(0,numerodifiguregeneriche)
    if printa:
        print(VetFig)
    #%facciamo 4 grafici:
    #%   1   geometria fino agli assi principali
    #%   2   geometria con assi principali ed  ellisse dinerzia
    #%   3   geometria con assi principali e nocciolo dinerzia
    #%   4   geometria con lo studio dell'asse neutro
    #%clf %cancella il grafico corrente
    #%alla fine uno e basta, che poi mi rompo
    scalatore=self.scalatore
    if scalatore!=1:
        traslax=scalatore*traslax
        traslay=scalatore*traslay
        listadicoordinatefinale=np.dot(scalatore,listadicoordinatefinale)
        baricentrototalex=scalatore*baricentrototalex
        baricentrototaley=scalatore*baricentrototaley
        puntopiulontanoyyy1=puntopiulontanoyyy1#*scalatore
        puntopiulontanoxxx1=puntopiulontanoxxx1#*scalatore
        puntopiulontanoyyy2=puntopiulontanoyyy2#*scalatore
        puntopiulontanoxxx2=puntopiulontanoxxx2#*scalatore
        sigmadelpuntopiulontano1=sigmadelpuntopiulontano1*scalatore
        sigmadelpuntopiulontano2=sigmadelpuntopiulontano2*scalatore
        #rhoeee=scalatore*rhoeee
        #rhonii=scalatore*rhonii
        puntopiulontanoyyy1=scalatore*puntopiulontanoyyy1
        puntopiulontanoxxx1=scalatore*puntopiulontanoxxx1
        puntopiulontanoyyy2=scalatore*puntopiulontanoyyy2
        puntopiulontanoxxx2=scalatore*puntopiulontanoxxx2
    if printa:
        print(puntopiulontanoxxx1)
        print(puntopiulontanoyyy1)
        print(puntopiulontanoxxx2)
        print(puntopiulontanoyyy2)
    limitexminimo=minimo(listadicoordinatefinale[:,0])
    limitexmassimo=massimo(listadicoordinatefinale[:,0])
    limiteyminimo=minimo(listadicoordinatefinale[:,1])
    limiteymassimo=massimo(listadicoordinatefinale[:,1])
    alfa=0.15*(limiteymassimo-limiteyminimo)
    beta=0.15*(limitexmassimo-limitexminimo)
    limitexminimo=limitexminimo-beta
    limitexmassimo=limitexmassimo+alfa
    limiteyminimo=limiteyminimo-beta
    limiteymassimo=limiteymassimo+alfa

    ciccio=((limitexmassimo-limitexminimo)+(limiteymassimo-limiteyminimo))*0.2
    assebaricentrototalex=(np.arange(0,11))
    assebaricentrototaley=(np.arange(0,11))
    assebaricentrototalenii=(np.arange(0,11))
    assebaricentrototaleeee=(np.arange(0,11))
    assebaricentrototalex[0]=limitexminimo
    assebaricentrototaley[0]=baricentrototaley
    assebaricentrototalex[1]=limitexmassimo
    assebaricentrototaley[1]=baricentrototaley
    assebaricentrototalex[2]=limitexmassimo-ciccio/10
    assebaricentrototaley[2]=baricentrototaley-ciccio/30
    assebaricentrototalex[3]=limitexmassimo-ciccio/10
    assebaricentrototaley[3]=baricentrototaley+ciccio/30
    assebaricentrototalex[4]=limitexmassimo
    assebaricentrototaley[4]=baricentrototaley
    assebaricentrototalex[5]=baricentrototalex
    assebaricentrototaley[5]=baricentrototaley
    assebaricentrototalex[6]=baricentrototalex
    assebaricentrototaley[6]=limiteyminimo
    assebaricentrototalex[7]=baricentrototalex
    assebaricentrototaley[7]=limiteymassimo
    assebaricentrototalex[8]=baricentrototalex-ciccio/30
    assebaricentrototaley[8]=limiteymassimo-ciccio/10
    assebaricentrototalex[9]=baricentrototalex+ciccio/30
    assebaricentrototaley[9]=limiteymassimo-ciccio/10
    assebaricentrototalex[10]=baricentrototalex
    assebaricentrototaley[10]=limiteymassimo
    assebaricentrototalenii[0]=(limitexminimo-baricentrototalex)*cos(-Aangolo_rad)+(0)*sin(-Aangolo_rad)+baricentrototalex
    assebaricentrototaleeee[0]=-(limitexminimo-baricentrototalex)*sin(-Aangolo_rad)+(0)*cos(-Aangolo_rad)+baricentrototaley
    assebaricentrototalenii[1]=(limitexmassimo-baricentrototalex)*cos(-Aangolo_rad)+(0)*sin(-Aangolo_rad)+baricentrototalex
    assebaricentrototaleeee[1]=-(limitexmassimo-baricentrototalex)*sin(-Aangolo_rad)+(0)*cos(-Aangolo_rad)+baricentrototaley
    assebaricentrototalenii[2]=(limitexmassimo-ciccio/10-baricentrototalex)*cos(-Aangolo_rad)+(0-ciccio/30)*sin(-Aangolo_rad)+baricentrototalex
    assebaricentrototaleeee[2]=-(limitexmassimo-ciccio/10-baricentrototalex)*sin(-Aangolo_rad)+(0-ciccio/30)*cos(-Aangolo_rad)+baricentrototaley
    assebaricentrototalenii[3]=(limitexmassimo-ciccio/10-baricentrototalex)*cos(-Aangolo_rad)+(0+ciccio/30)*sin(-Aangolo_rad)+baricentrototalex
    assebaricentrototaleeee[3]=-(limitexmassimo-ciccio/10-baricentrototalex)*sin(-Aangolo_rad)+(0+ciccio/30)*cos(-Aangolo_rad)+baricentrototaley
    assebaricentrototalenii[4]=(limitexmassimo-baricentrototalex)*cos(-Aangolo_rad)+(0)*sin(-Aangolo_rad)+baricentrototalex
    assebaricentrototaleeee[4]=-(limitexmassimo-baricentrototalex)*sin(-Aangolo_rad)+(0)*cos(-Aangolo_rad)+baricentrototaley
    assebaricentrototalenii[5]=(0)*cos(-Aangolo_rad)+(0)*sin(-Aangolo_rad)+baricentrototalex
    assebaricentrototaleeee[5]=-(0)*sin(-Aangolo_rad)+(0)*cos(-Aangolo_rad)+baricentrototaley
    assebaricentrototalenii[6]=(0)*cos(-Aangolo_rad)+(limiteyminimo-baricentrototaley)*sin(-Aangolo_rad)+baricentrototalex
    assebaricentrototaleeee[6]=-(0)*sin(-Aangolo_rad)+(limiteyminimo-baricentrototaley)*cos(-Aangolo_rad)+baricentrototaley
    assebaricentrototalenii[7]=(0)*cos(-Aangolo_rad)+(limiteymassimo-baricentrototaley)*sin(-Aangolo_rad)+baricentrototalex
    assebaricentrototaleeee[7]=-(0)*sin(-Aangolo_rad)+(limiteymassimo-baricentrototaley)*cos(-Aangolo_rad)+baricentrototaley
    assebaricentrototalenii[8]=(0-ciccio/30)*cos(-Aangolo_rad)+(limiteymassimo-ciccio/10-baricentrototaley)*sin(-Aangolo_rad)+baricentrototalex
    assebaricentrototaleeee[8]=-(0-ciccio/30)*sin(-Aangolo_rad)+(limiteymassimo-ciccio/10-baricentrototaley)*cos(-Aangolo_rad)+baricentrototaley
    assebaricentrototalenii[9]=(0+ciccio/30)*cos(-Aangolo_rad)+(limiteymassimo-ciccio/10-baricentrototaley)*sin(-Aangolo_rad)+baricentrototalex
    assebaricentrototaleeee[9]=-(0+ciccio/30)*sin(-Aangolo_rad)+(limiteymassimo-ciccio/10-baricentrototaley)*cos(-Aangolo_rad)+baricentrototaley
    assebaricentrototalenii[10]=(0)*cos(-Aangolo_rad)+(limiteymassimo-baricentrototaley)*sin(-Aangolo_rad)+baricentrototalex
    assebaricentrototaleeee[10]=-(0)*sin(-Aangolo_rad)+(limiteymassimo-baricentrototaley)*cos(-Aangolo_rad)+baricentrototaley
    #assebaricentrototalex=np.asmatrix(assebaricentrototalex)
    #assebaricentrototaley=np.asmatrix(assebaricentrototaley)
    #asse=UnireMatriciRig(transponi(assebaricentrototalex),transponi(assebaricentrototaley))  
    #aa=input("cazzo")
    assenullox=(np.arange(0,11))
    assenulloy=(np.arange(0,11))
    assenullox[0]=limitexminimo
    assenulloy[0]=0
    assenullox[1]=limitexmassimo
    assenulloy[1]=0
    assenullox[2]=limitexmassimo-ciccio/10
    assenulloy[2]=0-ciccio/30
    assenullox[3]=limitexmassimo-ciccio/10
    assenulloy[3]=0+ciccio/30
    assenullox[4]=limitexmassimo
    assenulloy[4]=0
    assenullox[5]=0
    assenulloy[5]=0
    assenullox[6]=0
    assenulloy[6]=limiteyminimo
    assenullox[7]=0
    assenulloy[7]=limiteymassimo
    assenullox[8]=0-ciccio/30
    assenulloy[8]=limiteymassimo-ciccio/10
    assenullox[9]=0+ciccio/30
    assenulloy[9]=limiteymassimo-ciccio/10
    assenullox[10]=0
    assenulloy[10]=limiteymassimo
    #assenullox=np.asmatrix(assenullox)
    #assenulloy=np.asmatrix(assenulloy)
    #print(type(assenulloy))
    
    #%assixy=[assenullox; assenulloy];
    #%numerogiust0 e' 100 ma anche 50 va molto bene
    """
    ellisse(:,1)=linspace(0,2*pi,100);
    ellisse(:,2)=(rhonii**0.5)*cos(ellisse(:,1));
    ellisse(:,3)=(rhoeee**0.5)*sin(ellisse(:,1));
    ellisse(:,4)=baricentrototalex+ellisse(:,2)*cos(-Aangolo_rad)+ellisse(:,3)*sin(-Aangolo_rad);
    ellisse(:,5)=baricentrototaley-ellisse(:,2)*sin(-Aangolo_rad)+ellisse(:,3)*cos(-Aangolo_rad);
    #%matrice_di_ellisse=[ellisse(:,4),ellisse(:,5)];    """
    if rhoeee>0 and rhonii>0:
        nop=100
        el3=np.arange(0,nop+1)
        el4=np.arange(0,nop+1)
        #ellisse=np.linspace(0,2*pi,nop,endpoint=True)
        #print(ellisse)
        #print(type(ellisse))
        Vet=range(0,nop)
        for i in Vet:
            angolo=2*pi*i/nop
            el1=el2=0
            el1=(rhonii**0.5)*(cos(angolo))
            el2=(rhoeee**0.5)*(sin(angolo))
            #print(i,angolo,el1,el2)
            el3[i]=baricentrototalex+scalatore*(+el1*(cos(-Aangolo_rad))+el2*(sin(-Aangolo_rad)))
            el4[i]=baricentrototaley+scalatore*(-el1*(sin(-Aangolo_rad))+el2*(cos(-Aangolo_rad)))
        angolo=2*pi
        i=i+1
        el1=(rhonii**0.5)*(cos(angolo))
        el2=(rhoeee**0.5)*(sin(angolo))
        el3[i]=baricentrototalex+scalatore*(+el1*(cos(-Aangolo_rad))+el2*(sin(-Aangolo_rad)))
        el4[i]=baricentrototaley+scalatore*(-el1*(sin(-Aangolo_rad))+el2*(cos(-Aangolo_rad)))
       # print(i,angolo,el1,el2)
    #print(noccioloordinato)
    #print(noccioloordinato)
    if vuoifareancheilnocciolo:
        #size2(noccioloordinato,0)
        neg=np.size(noccioloordinato,0)
        nocciolo1=np.arange(0,neg+1)
        nocciolo2=np.arange(0,neg+1)
        if printa:
            print(noccioloordinato)
        VetN=range(0,neg)
        for k in VetN:
            nocciolo1[k]=noccioloordinato[k,0]*scalatore
            nocciolo2[k]=noccioloordinato[k,1]*scalatore
            #print(k,noccioloordinato[k,0],noccioloordinato[k,1],nocciolo1[k],nocciolo2[k])
        nocciolo1[k+1]=noccioloordinato[0,0]*scalatore
        nocciolo2[k+1]=noccioloordinato[0,1]*scalatore
        if printa:
            print(nocciolo1,nocciolo2)
        #print(k,noccioloordinato[k,0],noccioloordinato[k,1],nocciolo1[k],nocciolo2[k])
        #nocciolox=[noccioloordinato(:,1);noccioloordinato(1,1)]
        #noccioloy=[noccioloordinato(:,2);noccioloordinato(1,2)]
    #print(nocciolo1)
    #print(nocciolo2)
    if vuoiplottare:
        import matplotlib.pyplot as plt
        #figsize=(11.69,8.27),dpi=600
        fig=plt.figure()
        #plt.clf()
        #plt.rcdefaults()
        if scherza:   
            plt.xkcd(scale=1, length=100, randomness=2,figure=fig)          
    if vuoiplottare:
        coordinate=0
        from calcolatrice.studiatore2 import studianumero1
        for i in VetFig:
            calcolo=5
            cacca=numero1[i,:]
            [coordinate,b1,b2,b3,b4,b5,b6,b7,b8,peso_specifico]=studianumero1(cacca,kk,calcolo,discretizzaarchicerchi,0,0)
            if peso_specifico>0:
                #print(coordinate)
                coordinate=np.dot(scalatore,coordinate)
                vettore=size2(coordinate,1)
                #0print(size2(coordinate,0))
                coordx=np.arange(0,vettore)
                #print(coordx)
                coordy=np.arange(0,vettore)
                VetVettore=range(0,vettore)
                for j in VetVettore:
                    coordx[j]=coordinate[j,0]
                    coordy[j]=coordinate[j,1]
                if vuoiplottare:
                    if printa:
                        print(coordx,coordy)                    #plt.plot(coordx,coordy,"black")
                    plt.plot(coordx,coordy,"black", alpha=1,figure=fig)
                    plt.fill(coordx,coordy,"red", alpha=0.8,figure=fig)
                    figure_wgt = self.root.ids['figure_wgt']  # MatplotFigure
                    figure_wgt.figure = fig
                    #plt.fill(x,y)
                    #patch(coordinate(:,1)-traslax,coordinate(:,2)-traslay,"red")
        for i in VetFig:
            calcolo=5
            cacca=numero1[i,:]
            [coordinate,b1,b2,b3,b4,b5,b6,b7,b8,peso_specifico]=studianumero1(cacca,kk,calcolo,discretizzaarchicerchi,0,0)
            if peso_specifico<0:
                #print(coordinate)
                coordinate=np.dot(scalatore,coordinate)
                vettore=size2(coordinate,1)
                #0print(size2(coordinate,0))
                coordx=np.arange(0,vettore)
                #print(coordx)
                coordy=np.arange(0,vettore)
                VetVettore=range(0,vettore)
                for j in VetVettore:
                    coordx[j]=coordinate[j,0]
                    coordy[j]=coordinate[j,1]
                if vuoiplottare:
                    if printa:
                        print(coordx,coordy)
                    #plt.plot(coordx,coordy,"black")
                    plt.fill(coordx,coordy,"white", alpha=1,figure=fig)
                    plt.plot(coordx,coordy,"white", alpha=1,figure=fig)
                    figure_wgt = self.root.ids['figure_wgt']  # MatplotFigure
                    figure_wgt.figure = fig
        if 0:
            plt.plot(assenullox,assenulloy,"-",figure=fig)    
            plt.text(assenullox[1]+0.05,assenulloy[1],'Xo',figure=fig)
            plt.text(assenullox[8],assenulloy[8],'Yo',figure=fig)
            plt.fill(assenullox[1:4],assenulloy[1:4],"blue",alpha=1,figure=fig)
            plt.fill(assenullox[7:10],assenulloy[7:10],"blue",alpha=1,figure=fig)
        plt.plot(assebaricentrototalenii,assebaricentrototaleeee,"green",figure=fig)    
        plt.fill(assebaricentrototalenii[1:4],assebaricentrototaleeee[1:4],"green",figure=fig)    
        plt.fill(assebaricentrototalenii[7:10],assebaricentrototaleeee[7:10],"green",figure=fig)    
        #plt.text(assebaricentrototaleeee[1]-traslax,assebaricentrototalenii[1]-traslay,'Xi')
        #plt.text(assebaricentrototaleeee[8]-traslax,assebaricentrototalenii[8]-traslay,'Yi')
        plt.plot(assebaricentrototalex,assebaricentrototaley,"black")
        plt.fill(assebaricentrototalex[1:4],assebaricentrototaley[1:4],"black",alpha=1,figure=fig)
        plt.fill(assebaricentrototalex[7:10],assebaricentrototaley[7:10],"black",alpha=1,figure=fig)
        plt.text(limitexmassimo,baricentrototaley-0.05,'Xg',figure=fig)
        plt.text(baricentrototalex,limiteymassimo,'Yg',figure=fig)
			#plt.xlim([nuovolixmin,nuovolixmax])
        #plt.ylim([nuovoliymin,nuovoliymax])
        plt.plot(el3,el4,"green",figure=fig)
        plt.fill(el3,el4, "black", alpha=0.1,figure=fig)
        figure_wgt = self.root.ids['figure_wgt']  # MatplotFigure
        figure_wgt.figure = fig
        if vuoifareancheilnocciolo:
            plt.plot(nocciolo1,nocciolo2,"black",figure=fig)
            plt.fill(nocciolo1,nocciolo2,"black",alpha=0.5,figure=fig)
            figure_wgt = self.root.ids['figure_wgt']  # MatplotFigure
            figure_wgt.figure = fig
#######################################################################################

    if sollecitazione[0,0]==1 or sollecitazione[0,0]==2:
        #%angolo della traslazione del SdR            Aangolo_rad
        #%angolo della retta di nullomassimox         angolo_rad
        ptx1=assenullox[0]
        pty1=assenulloy[0]
        ptx2=assenullox[1]
        pty2=assenulloy[1]
        if printa:
            print(Aangolo_rad,angolo_rad,pi/2)
        tootale=-Aangolo_rad-angolo_rad-pi/2
        rettadinullox=np.arange(0,2)
        rettadinulloy=np.arange(0,2)
        rettadinullox[0]=+(ptx1)*cos(tootale)+(pty1)*sin(tootale)+baricentrototalex
        rettadinulloy[0]=-(ptx1)*sin(tootale)+(pty1)*cos(tootale)+baricentrototaley
        rettadinullox[1]=+(ptx2)*cos(tootale)+(pty2)*sin(tootale)+baricentrototalex
        rettadinulloy[1]=-(ptx2)*sin(tootale)+(pty2)*cos(tootale)+baricentrototaley
        emmenulla=(rettadinulloy[0]-rettadinulloy[1])/(rettadinullox[0]-rettadinullox[1])
        quellanulla=rettadinulloy[1]-emmenulla*rettadinullox[1]
        pluslmax=np.abs((limitexmassimo-limitexminimo)/20)
        pluslmin=np.abs((limitexmassimo-limitexminimo)/20)
        rettadinullox[0]=limitexminimo-pluslmin
        rettadinullox[1]=limitexmassimo+pluslmax
        rettadinulloy[0]=rettadinullox[0]*emmenulla+quellanulla
        rettadinulloy[1]=rettadinullox[1]*emmenulla+quellanulla
        #print(rettadinullox,rettadinulloy)
        #%il valore qui sotto non è giusto
        if emmenulla==0:
            quellanormale=9999999999999
        else:
            quellanormale=rettadinulloy[0]-(-1/emmenulla)*(rettadinullox[0])
        quella1=puntopiulontanoyyy1-emmenulla*puntopiulontanoxxx1
        limxnormale1=(quellanormale-quella1)/(emmenulla+1/emmenulla)
        limynormale1=limxnormale1*emmenulla+quella1
        quella2=puntopiulontanoyyy2-emmenulla*puntopiulontanoxxx2
        limxnormale2=(quellanormale-quella2)/(emmenulla+1/emmenulla)
        limynormale2=limxnormale2*emmenulla+quella2
        rettanormalex=np.arange(0,4)
        rettanormaley=np.arange(0,4)
        rettanormalex[0]=puntopiulontanoxxx1
        rettanormalex[1]=limxnormale1
        rettanormalex[2]=limxnormale2
        rettanormalex[3]=puntopiulontanoxxx2
        rettanormaley[0]=puntopiulontanoyyy1
        rettanormaley[1]=limynormale1
        rettanormaley[2]=limynormale2
        rettanormaley[3]=puntopiulontanoyyy2
        #%sigmadelpuntopiulontano2=-1572.25;
        #%sigmadelpuntopiulontano1=2438.17;
        #%angolo_nullo=atan2(rettadinulloy(2)-rettadinulloy(1),rettadinullox(2)-rettadinullox(1));
        fractor=800
        salto2=sigmadelpuntopiulontano2
        posixpt1x=limxnormale1-(sigmadelpuntopiulontano1/fractor)*(cos(-tootale))
        posixpt1y=limynormale1-(sigmadelpuntopiulontano1/fractor)*(sin(-tootale))
        posixpt2x=limxnormale2-(salto2/fractor)*(cos(-tootale))
        posixpt2y=limynormale2-(salto2/fractor)*(sin(-tootale))
        farfallax=np.arange(0,4)
        farfallay=np.arange(0,4)
        farfallax[0]=limxnormale1
        farfallax[1]=posixpt1x
        farfallax[2]=posixpt2x
        farfallax[3]=limxnormale2
        farfallay[0]=limynormale1
        farfallay[1]=posixpt1y
        farfallay[2]=posixpt2y
        farfallay[3]=limynormale2
        #str=['Sigma=  ',num2str(x.sigmadelpuntopiulontano1)]
        #text(posixpt1x+0.5,posixpt1y+0.5,str);
        #str=['Sigma=  ',num2str(x.sigmadelpuntopiulontano2)]
        #text(posixpt2x-0.5,posixpt2y,str,'horizontalalignment', 'right')
        plt.plot(rettadinullox,rettadinulloy,'-.',figure=fig)
        plt.plot(rettanormalex,rettanormaley,'-.',figure=fig)
        plt.fill(farfallax,farfallay,'black',figure=fig)
        figure_wgt = self.root.ids['figure_wgt']  # MatplotFigure
        figure_wgt.figure = fig
        #plt.title("Cercami su Facebook digitando Code:Section")
            

    #if 0:
        #from matplotlib import rc
        #rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
        #rc('text', usetex=True)
    #else:
        #plt.rc('text', usetex=False)
    
    #plt.title(stringa,loc="left")
    #plt.plot(el3,el4,"g")

    #fig.set_size_inches([11.69,8.27])
    #plt.grid(True)
    #plt.autoscale(True)
    #plt.yscale('linear')
    #plt.xscale('linear')
    #plt.show(fig)

    #if 0:
        #import os
        #a=os.getcwd()
        #os.chdir(a+"\\risultati")
        #from pathlib import Path
        #import os
        #via=os.getcwd()
        #if printa:
        #    print(via)
        #os.chdir(Path(via).parent)
        #print(os.chdir(Path(via).parent))
        #if printa:
            #print("beeeeeh")
        #fig.savefig("ciccio.png", dpi=600)
        #plt.close(fig) 
        #os.chdir(via)
    """                  
    %text(assebaricentrototalex(2)-0.5,assebaricentrototaley(2),'Xo');
    %text(assebaricentrototalex(5),assebaricentrototaley(5),'Yo');
    """                        
    return  1
