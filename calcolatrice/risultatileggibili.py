def RisToString(noccioloordinato,vuoifareancheilnocciolo,areatotale,baricentrototalex,\
                            baricentrototaley,essex,essey,matrice_inerzia_totale,\
                            Aangolo_rad,Aangolo_gon,Aangolo_grad,rhoeee,rhonii,\
                            casoinesame,inerziaeee,inerzianii):
    ##%stampatore dei parametri importanti, tramite print in un file di testo txt formattato
    import numpy as np
    from calcolatrice.misuras import size2
    """
    areatotale=4253.5234
    baricentrototalex=20.58168
    baricentrototaley=42.056468
    essex=245.0548
    essey=846.1561
    matrice_inerzia_totale=np.matrix("0 0 0 0")
    matrice_inerzia_totale[0,0]=5284.54846
    matrice_inerzia_totale[0,1]=5114411.54846
    matrice_inerzia_totale[0,2]=414.54846
    matrice_inerzia_totale[0,3]=5165.54846
    Aangolo_rad=1.5168
    Aangolo_gon=1.51181
    Aangolo_grad=0.216818
    rhoeee=5.4243333
    rhonii=4.33333
    casoinesame=19
    inerziaeee=15.2168
    inerzianii=48.2286
    #%h=find(nomArch==".");
    #%nomTxt=nomArch;
    #%nomTxt(1,h+1:h+3)="txt";
    #%init="risultati\\";
    #%nomTxt=[init,nomTxt];
    #%aa=fopen(nomTxt,"wt");
    #aa=fopen("risultati\leggifacile.txt","wt")
    #triple quote per tutti
    """
    #import string as str
    stringa=""
    #stringa=stringa+"""Codice di calcolo dei parametri geometrici di una sezione piana.\n"""
    #title("My name is %s and weight is %d kg!" % ('Zara', 21) )
    #è un numero?
    """
    print(str.isnumeric(stringa))
    #quanti caratteri ci sono?
    print(str.count(stringa,0,len(stringa)))
    #cerca un oggetto dentro un altro oggetto
    #una stringa dentro un'altra stringa
    str1="aaacddderrr"
    str2="rr"
    print(str1.find(str2,0,len(str1)))
    """

    stringa=stringa+"""A=%6.3f \n""" %areatotale
    stringa=stringa+"""MSY=%6.3f\n""" %essey
    stringa=stringa+"""MSX=%6.3f\n""" %essex
    stringa=stringa+"""Xg=%6.3f\n""" %baricentrototalex
    stringa=stringa+"""Yg=%6.3f\n""" %baricentrototaley
    stringa=stringa+"""Ixg=%6.3f\n""" %matrice_inerzia_totale[0,3]
    stringa=stringa+"""Iyg=%6.3f\n""" %matrice_inerzia_totale[0,0]
    stringa=stringa+"""Ixgyg=%6.3f\n""" %matrice_inerzia_totale[0,1]
    stringa=stringa+"""Theta=%6.3f /360\n""" %Aangolo_grad
    #stringa=stringa+"""Assi Principali di Inerzia \n"""
    if casoinesame==11:
        stringa=stringa+"""Inii=%6.3f\n"""%inerziaeee
        stringa=stringa+"""Ieee=%6.3f\n"""%inerzianii
    elif casoinesame==15:
        stringa=stringa+"""Inii=%6.3f\n"""%inerziaeee
        stringa=stringa+"""Ieee=%6.3f\n"""%inerzianii
    elif casoinesame==19:
        stringa=stringa+"""Inii=%6.3f\n"""%inerziaeee
        stringa=stringa+"""Ieee=%6.3f\n"""%inerzianii
    stringa=stringa+"""rho2 eee=%6.3f\n"""%rhoeee
    stringa=stringa+"""rho2 nii=%6.3f\n"""%rhonii
    stringa=stringa+"""rho  eee=%6.3f\n"""%rhoeee**0.5
    stringa=stringa+"""rho  nii=%6.3f\n"""%rhonii**0.5

    if vuoifareancheilnocciolo:
        onlyeq=1
        numtangenti=size2(noccioloordinato,1)
        VetN=range(0,numtangenti)
        #print(noccioloordinato.T)
        stringa=stringa+"""\n"""
        if onlyeq==0:
            stringa=stringa+"""Rette tangenti, Coordinate Totali e Baricentriche degli antipoli %g:\n"""%numtangenti
        else:
            stringa=stringa+"""Tang %g:\n"""%numtangenti
        if numtangenti>10:
            verbose_mode_tangenti=0
        else:
            verbose_mode_tangenti=1
        if verbose_mode_tangenti==1:
            if onlyeq==0:
                stringa=stringa+"""X Baric\t\t  Y Baric\t\tX Totale\t  Y Totale\t\teq. rette tangenti\n"""
                for punti in VetN:
                    #print(punti,noccioloordinato[punti,11],noccioloordinato[punti,12])
                    stringa=stringa+"""x=%6.2f \t"""%noccioloordinato[punti,11]
                    stringa=stringa+"""y=%6.2f \t\t"""%noccioloordinato[punti,12]
                    stringa=stringa+"""x=%6.2f \t"""%noccioloordinato[punti,0]
                    stringa=stringa+"""  y=%6.2f \t\t"""%noccioloordinato[punti,1]
                    if noccioloordinato[punti,8]==1:
                        stringa=stringa+"""x=%6.3f"""%noccioloordinato[punti,9]
                    elif noccioloordinato[punti,8]==2:
                        stringa=stringa+"""y=%6.3f"""%noccioloordinato[punti,9]
                    elif noccioloordinato[punti,8]==3:
                        stringa=stringa+"""(%6.3f)x""" %noccioloordinato[punti,8]
                        stringa=stringa+"""+(%6.3f)y""" %noccioloordinato[punti,9]
                        stringa=stringa+"""+(%6.3f)=0""" %noccioloordinato[punti,10]
                    stringa=stringa+"""\n"""
            else:
                for punti in VetN:
                    if noccioloordinato[punti,8]==1.:
                        stringa=stringa+"""x=%6.3f"""%noccioloordinato[punti,9]
                        stringa=stringa+"""\n"""
                    elif noccioloordinato[punti,8]==2.:
                        stringa=stringa+"""y=%6.3f"""%noccioloordinato[punti,9]
                        stringa=stringa+"""\n"""
                    else:#if noccioloordinato[punti,8]==3.:
                        stringa=stringa+"""(%6.1f)x""" %noccioloordinato[punti,8]
                        stringa=stringa+"""+(%6.1f)y""" %noccioloordinato[punti,9]
                        stringa=stringa+"""+(%6.1f)=0""" %noccioloordinato[punti,10]
                        stringa=stringa+"""\n"""
        else:
            stringa=stringa+"""il nocciolo viene solo disegnato\n"""
    stringa=stringa+"""Un progetto di Biancardi Francesco Gennaio2017\n"""
    #stringa=stringa+"""https://www.facebook.com/francescoscodesection\n"""
    return stringa