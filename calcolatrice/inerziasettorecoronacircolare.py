def InerSettCoronCir(raggio,angolof,angoloi,coordxc,coordyc):
    import numpy as np
    from math import pi, cos, sin
    while angoloi>2*pi:
        angoloi=angoloi-2*pi
    while angoloi<0:
        angoloi=angoloi+2*pi
    while angolof>2*pi:
        angolof=angolof-2*pi
    while angolof<0:
        angoloi=angoloi+2*pi
    nega=0
    if angoloi>angolof:
        nega=1
        caso=angoloi
        angoloi=angolof
        angolof=caso
    angolo=angolof-angoloi
    momenti_staticix=(raggio**3)*(-cos(angolof)+cos(angoloi))/3
    momenti_staticiy=(raggio**3)*(sin(angolof)-sin(angoloi))/3
    momenti_statici=np.zeros((1,2))
    momenti_statici[0,0]=momenti_staticix
    momenti_statici[0,1]=momenti_staticiy
    area=(angolof-angoloi)*(raggio**2)/2
    baricentrox=momenti_staticiy/area
    baricentroy=momenti_staticix/area
    inerzia_lungox=(raggio**4)*(angolo-(cos(angolof))*(sin(angolof))+(cos(angoloi))*(sin(angoloi)))/8+(area*baricentroy*baricentroy)-2*momenti_staticix*(baricentroy)
    inerzia_lungoy=(raggio**4)*(angolo+(cos(angolof))*(sin(angolof))-(cos(angoloi))*(sin(angoloi)))/8+(area*baricentrox*baricentrox)-2*momenti_staticiy*(baricentrox)
    inerzia_lungoxy=(raggio**4)*(((sin(angolof))**2)-((sin(angoloi))**2))/16+(area*baricentrox*baricentroy)-momenti_staticix*baricentrox-momenti_staticiy*baricentroy
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    matrice_inerzia=np.asmatrix(np.zeros((2,2)))
    matrice_inerzia[0,0]=inerzia_lungoy
    matrice_inerzia[0,1]=inerzia_lungoxy
    matrice_inerzia[1,0]=inerzia_lungoxy
    matrice_inerzia[1,1]=inerzia_lungox
    baricentrox=baricentrox+coordxc
    baricentroy=baricentroy+coordyc
    if nega:
        momenti_staticicerchio=np.matrix("0 0")
        areacerchio=pi*(raggio**2)
        matrice_inerziacerchio=np.zeros((2,2))
        matrice_inerziacerchio[0,0]=pi*(raggio**4)/4
        matrice_inerziacerchio[1,1]=matrice_inerziacerchio[0,0]
        baricentroxcerchio=coordxc
        baricentroycerchio=coordyc
        baricentrox=(areacerchio*baricentroxcerchio-area*baricentrox)/(areacerchio-area)
        baricentroy=(areacerchio*baricentroycerchio-area*baricentroy)/(areacerchio-area)
        matrice_inerzia=matrice_inerziacerchio-matrice_inerzia
        momenti_statici=momenti_staticicerchio-momenti_statici
        area=areacerchio-area
    #print("cicccc",baricentrox,baricentroy,area,momenti_statici,matrice_inerzia)
    return baricentrox,baricentroy,area,momenti_statici,matrice_inerzia