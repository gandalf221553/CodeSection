# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 18:25:29 2017

@author: Von Braun
"""

def disegna(self,numero1):
    #print(numero1)
    #print(listadicoordinatefinale)
    #function poltrire(numero1,kk,nomArch,discretizzaarchicerchi,vuoifareancheilnocciolo,noccioloordinato,listadicoordinatefinale,traslax,traslay,sollecitazione,x)
    kk=numero1[0,1]
    discretizzaarchicerchi=numero1[0,3]
    vuoiplottare=1
    scherza=0
    printa=0
    #%x.Aangolo_rad %quello dellasse neutro
    #%x.angolo_rad %quello della solleciazione
    import numpy as np
    from calcolatrice.misuras import size2
    numerodifiguregeneriche=size2(numero1,1) # % dimmi quante figure vuoi inserire
    VetFig=range(1,numerodifiguregeneriche)
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
    import matplotlib.pyplot as plt
    #figsize=(11.69,8.27),dpi=600
    fig=plt.figure()
    #plt.clf()
    #plt.rcdefaults()
    if scherza:   
        plt.xkcd(scale=1, length=100, randomness=2,figure=fig)
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
                plt.plot(coordx,coordy,"black", alpha=1,rasterized=True,figure=fig)
                plt.fill(coordx,coordy,"red", alpha=0.8,rasterized=True,figure=fig)
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
                plt.fill(coordx,coordy,"white", alpha=1,rasterized=True,figure=fig)
                plt.plot(coordx,coordy,"white", alpha=1,rasterized=True,figure=fig)
                figure_wgt = self.root.ids['figure_wgt']  # MatplotFigure
                figure_wgt.figure = fig
                #patch(coordinate(:,1)-traslax,coordinate(:,2)-traslay,"white")            

    #fig.set_size_inches([11.69,8.27])
    #plt.axis('off')
    #plt.grid(False)        
    #plt.autoscale(True)
    #plt.yscale('linear')
    #plt.xscale('linear')
    #plt.show(fig)

    if 0:
        if printa:
            print("beeeeeh")
        fig.savefig("solooggetto.png", dpi=600)
        plt.close(fig) 
        #os.chdir(via)
    """                  
    %text(assebaricentrototalex(2)-0.5,assebaricentrototaley(2),'Xo');
    %text(assebaricentrototalex(5),assebaricentrototaley(5),'Yo');
    """                        
    return  1