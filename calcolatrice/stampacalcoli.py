function stampacalcoli(x)
%stampatore di tutti i valori da produrre
cd risultati
%nella variabile di entrata ci vogliono tutti i valori 
aa = fopen ('geometrypluscalcolous.txt','wt');
%stampa della somma delle aree
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fprintf(aa,'Aree=%6.3f\n',x.areatotale);
fprintf(aa,'=(%6.3f',x.vettore_area_is(1));
%if numerodifiguregeneriche/=1 | numerodifiguregeneriche/=0
	if x.numerodifiguregeneriche>1
		for i=2:x.numerodifiguregeneriche
		fprintf(aa,'+%6.3f',x.vettore_area_is(i));
		end
	end
	fprintf(aa,')=%6.3f\n',x.areatotale);

	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%coordinata x del baricentro
fprintf(aa,'Coord. Xg=%6.3f\n',x.baricentrototalex);
fprintf(aa,'=[%6.3f*(%6.3f)',x.vettore_area_is(1),x.vettore_baricentrix(1));
%if numerodifiguregeneriche/=1 | numerodifiguregeneriche/=0
	if x.numerodifiguregeneriche>1
		for i=2:x.numerodifiguregeneriche
		fprintf(aa,'+%6.3f*(%6.3f)',x.vettore_area_is(i),x.vettore_baricentrix(i));
		end
	end
	fprintf(aa,']/(');
	
	fprintf(aa,'%6.3f',x.vettore_area_is(1));
	if x.numerodifiguregeneriche>1
		for i=2:x.numerodifiguregeneriche
		fprintf(aa,'+%6.3f',x.vettore_area_is(i));
		end
	end
	fprintf(aa,')=\n');
	fprintf(aa,'=%6.3f/%6.3f=%6.3f\n',x.essey,x.areatotale,x.baricentrototalex);
	%coordinata y del baricentro
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fprintf(aa,'Coord. Yg=%6.3f\n',x.baricentrototaley);
fprintf(aa,'=[%6.3f*(%6.3f)',x.vettore_area_is(1),x.vettore_baricentriy(1));
%if numerodifiguregeneriche/=1 | numerodifiguregeneriche/=0
	if x.numerodifiguregeneriche>1
		for i=2:x.numerodifiguregeneriche
		fprintf(aa,'+%6.3f*(%6.3f)',x.vettore_area_is(i),x.vettore_baricentriy(i));
		end
	end
	fprintf(aa,']/(');
	
	fprintf(aa,'%6.3f',x.vettore_area_is(1));
	if x.numerodifiguregeneriche>1
		for i=2:x.numerodifiguregeneriche
		fprintf(aa,'+%6.3f',x.vettore_area_is(i));
		end
	end
	fprintf(aa,')=\n');
	fprintf(aa,'=%6.3f/%6.3f=%6.3f\n',x.essex,x.areatotale,x.baricentrototaley);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%coordinataIxx della matrice  d'inerzia
fprintf(aa,'Inerzia Xg= %6.3f\n',x.matrice_inerzia_totale(1,4) );
fprintf(aa,'=(%6.3f',x.vet_m_inerzia_is(1,4));
%if numerodifiguregeneriche/=1 | numerodifiguregeneriche/=0
	if x.numerodifiguregeneriche>1
		for i=2:x.numerodifiguregeneriche
		fprintf(aa,'+%6.3f',x.vet_m_inerzia_is(i,4));
		end
	end	
	fprintf(aa,')+(%6.3f',x.vet_m_inerzia_huygens(1,4));
	if x.numerodifiguregeneriche>1
		for i=2:x.numerodifiguregeneriche
		fprintf(aa,'+%6.3f',x.vet_m_inerzia_huygens(i,4));
		end
	end	
	fprintf(aa,')=%6.3f\n',x.matrice_inerzia_totale(1,4));
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%coordinata yy della matrice  d'inerzia
fprintf(aa,'Inerzia Yg= %6.3f\n',x.matrice_inerzia_totale(1,1) );

fprintf(aa,'=(%6.3f',x.vet_m_inerzia_is(1,1));
%if numerodifiguregeneriche/=1 | numerodifiguregeneriche/=0
	if x.numerodifiguregeneriche>1
		for i=2:x.numerodifiguregeneriche
		fprintf(aa,'+%6.3f',x.vet_m_inerzia_is(i,1));
		end
	end	
	fprintf(aa,')+(%6.3f',x.vet_m_inerzia_huygens(1,1));
	if x.numerodifiguregeneriche>1
		for i=2:x.numerodifiguregeneriche
		fprintf(aa,'+%6.3f',x.vet_m_inerzia_huygens(i,1));
		end
	end	
	fprintf(aa,')=%6.3f\n',x.matrice_inerzia_totale(1,1));
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%coordinataIxy della matrice  d'inerzia
fprintf(aa,'Inerzia XgYg= %6.3f\n',x.matrice_inerzia_totale(1,2) );
fprintf(aa,'=(%6.3f',x.vet_m_inerzia_is(1,2));
%if numerodifiguregeneriche/=1 | numerodifiguregeneriche/=0
	if x.numerodifiguregeneriche>1
		for i=2:x.numerodifiguregeneriche
		fprintf(aa,'+%6.3f',x.vet_m_inerzia_is(i,2));
		end
	end	
	fprintf(aa,')+(%6.3f',x.vet_m_inerzia_huygens(1,2));
	if x.numerodifiguregeneriche>1
		for i=2:x.numerodifiguregeneriche
		fprintf(aa,'+%6.3f',x.vet_m_inerzia_huygens(i,2));
		end
	end	
	fprintf(aa,')=%6.3f\n',x.matrice_inerzia_totale(1,2));
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fprintf(aa,'\n');

fprintf(aa,'Angolo principale (antiorario)=\n=0.5*arctan((2*%6.3f)/(%6.3f-%6.3f))=\n',x.matrice_inerzia_totale(1,2),x.matrice_inerzia_totale(1,1),x.matrice_inerzia_totale(1,4));
%fprintf(aa,'=%6.3f (in radianti 2pi)\n',x.Aangolo_rad);
%fprintf(aa,'=%6.3f (in gon 400)\n',x.Aangolo_gon);
fprintf(aa,'=%6.3f (in grad 360)\n\n',x.Aangolo_grad);


fprintf(aa,'\n');

if x.casoinesame==11
fprintf(aa,'inerzia x>inerzia y\n%6.3f>%6.3f\n',x.matrice_inerzia_totale(1,4),x.matrice_inerzia_totale(1,1));
fprintf(aa,'Inerzia eee=%6.3f+%6.3f=\n',x.parametroaa,x.parametrobb);
fprintf(aa,'=%6.3f\n',x.inerziaeee);
fprintf(aa,'Inerzia nii=%6.3f-%6.3f=\n',x.parametroaa,x.parametrobb);
fprintf(aa,'=%6.3f\n',x.inerzianii);
elseif x.casoinesame==15
fprintf(aa,'inerzia x<inerzia y\n%6.3f<%6.3f\n',x.matrice_inerzia_totale(1,4),x.matrice_inerzia_totale(1,1));
fprintf(aa,'Inerzia eee=%6.3f-%6.3f =\n',x.parametroaa,x.parametrobb);
fprintf(aa,'= %6.3f \n',x.inerziaeee);
fprintf(aa,'Inerzia nii=%6.3f+%6.3f=\n',x.parametroaa,x.parametrobb);
fprintf(aa,'= %6.3f \n',x.inerzianii);
elseif x.casoinesame==19
fprintf(aa,'inerzia x=inerzia y\n%6.3f=%6.3f\n',x.matrice_inerzia_totale(1,4),x.matrice_inerzia_totale(1,1));
fprintf(aa,'Inerzia eee=%6.3f+%6.3f=\n',x.parametroaa,x.parametrobb);
fprintf(aa,'= %6.3f \n',x.inerziaeee);
fprintf(aa,'Inerzia nii=%6.3f-%6.3f=\n',x.parametroaa,x.parametrobb);
fprintf(aa,'=%6.3f\n\n',x.inerzianii);
end

fprintf(aa,'raggio quadro eee = %6.3f\n',x.rhoeee);
fprintf(aa,'raggio quadro nii = %6.3f\n\n',x.rhonii);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%parte di sollecitazione
if x.tipo==2
x.direzionedelmomento=x.attata-x.Aangolo_rad;
fprintf(aa,'Angolo del momento=\n');
%fprintf(aa,'= %6.3f (in radianti 2pi)\n',x.attata);
x.attata=x.attata*200/pi;
%fprintf(aa,'= %6.3f (in gon 400)\n',x.attata);
x.attata=x.attata/200*180;
fprintf(aa,'= %6.3f (in grad 360)\n\n',x.attata);

fprintf(aa,'momento eee =%6.3f\n',x.momentoeee);
fprintf(aa,'=%6.3fcos(%6.3f) =%6.3f\n',x.momento,x.attata,x.momentoeee);
fprintf(aa,'momento nii =%6.3f\n',x.momentonii);
fprintf(aa,'=%6.3fsin(%6.3f)=%6.3f\n',x.momento,x.attata,x.momentonii);

fprintf(aa,'\n');
fprintf(aa,'Asse Neutro \n');
fprintf(aa,'(%6.3f/%6.3f)nii-(%6.3f/%6.3f)eee=0\n',x.momentoeee,x.inerziaeee,x.momentonii,x.inerzianii);
fprintf(aa,'[nii=%6.3feee]\n\n\n',x.m);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	if x.sigmadelpuntopiulontano1>x.sigmadelpuntopiulontano2
	fprintf(aa,'le coordinate del punto di sforzo maggiore positivo:\n');
	elseif x.sigmadelpuntopiulontano1<x.sigmadelpuntopiulontano2
	fprintf(aa,'le coordinate del punto di sforzo maggiore negativo:\n');
	end

fprintf(aa,'[xxx,yyy]=[%6.3f,%6.3f] \n',x.puntopiulontanoxxx1,x.puntopiulontanoyyy1);
fprintf(aa,'eee =(%6.3f-%6.3f)cos(%6.3f)+(%6.3f-%6.3f)sin(%6.3f)=%6.3f\n',x.puntopiulontanoxxx1,x.baricentrototalex,x.Aangolo_grad,x.puntopiulontanoyyy1,x.baricentrototaley,x.Aangolo_grad,x.puntopiulontanoeee1);
fprintf(aa,'nii =-(%6.3f-%6.3f)sin(%6.3f)+(%6.3f-%6.3f)cos(%6.3f)=%6.3f\n',x.puntopiulontanoxxx1,x.baricentrototalex,x.Aangolo_grad,x.puntopiulontanoyyy1,x.baricentrototaley,x.Aangolo_grad,x.puntopiulontanonii1);
fprintf(aa,'[eee,nii]=[%6.3f,%6.3f]\n\n',x.puntopiulontanoeee1,x.puntopiulontanonii1);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	if x.sigmadelpuntopiulontano1>x.sigmadelpuntopiulontano2
	fprintf(aa,'le coordinate del punto di sforzo maggiore negativo: \n');
	elseif x.sigmadelpuntopiulontano1<x.sigmadelpuntopiulontano2
	fprintf(aa,'le coordinate del punto di sforzo maggiore positivo: \n');
	end

fprintf(aa,'[xxx,yyy]=[%6.3f,%6.3f]\n',x.puntopiulontanoxxx2,x.puntopiulontanoyyy2);
fprintf(aa,'eee=(%6.3f-%6.3f)cos(%6.3f)+(%6.3f-%6.3f)sin(%6.3f)=%6.3f\n',x.puntopiulontanoxxx2,x.baricentrototalex,x.Aangolo_grad,x.puntopiulontanoyyy2,x.baricentrototaley,x.Aangolo_grad,x.puntopiulontanoeee2);
fprintf(aa,'nii=-(%6.3f-%6.3f)sin(%6.3f)+(%6.3f-%6.3f)cos(%6.3f)=%6.3f\n',x.puntopiulontanoxxx2,x.baricentrototalex,x.Aangolo_grad,x.puntopiulontanoyyy2,x.baricentrototaley,x.Aangolo_grad,x.puntopiulontanonii2);
fprintf(aa,'[eee,nii]=[%6.3f,%6.3f]\n\n',x.puntopiulontanoeee2,x.puntopiulontanonii2);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	%stampa degli sforzi
	if x.sigmadelpuntopiulontano1>x.sigmadelpuntopiulontano2
	fprintf(aa,'sforzo maggiore positivo:\n');
	elseif x.sigmadelpuntopiulontano1<x.sigmadelpuntopiulontano2
	fprintf(aa,'sforzo maggiore negativo:\n');
	end
	fprintf(aa,'=(%6.3f/%6.3f)*%6.3f+(%6.3f/%6.3f)*(%6.3f)=\n',x.momentoeee,x.inerziaeee,x.puntopiulontanonii1,x.momentonii,x.inerziaeee,x.puntopiulontanoeee1);
	fprintf(aa,'=(%6.3f-(%6.3f))=%6.3f\n',x.termine2,x.termine3,x.sigmadelpuntopiulontano1);

	if x.sigmadelpuntopiulontano1>x.sigmadelpuntopiulontano2
	fprintf(aa,'sforzo maggiore negativo:\n');
	elseif x.sigmadelpuntopiulontano1<x.sigmadelpuntopiulontano2
	fprintf(aa,'sforzo maggiore positivo:\n');
	end
	fprintf(aa,'=(%6.3f/%6.3f)*%6.3f+(%6.3f/%6.3f)*(%6.3f)=\n',x.momentoeee,x.inerziaeee,x.puntopiulontanonii2,x.momentonii,x.inerziaeee,x.puntopiulontanoeee2);
	fprintf(aa,'=(%6.3f-(%6.3f))=%6.3f\n\n',x.termine4,x.termine5,x.sigmadelpuntopiulontano2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
elseif x.tipo==1

fprintf(aa,'coordinata del punto di applicazione = \n');
fprintf(aa,'[xxx,yyy]=[%6.3f,%6.3f]\n\n',x.punto_x_di_applicazione,x.punto_y_di_applicazione);
fprintf(aa,'eee=(%6.3f-%6.3f)cos(%6.3f)+(%6.3f-%6.3f)sin(%6.3f)=%6.3f\n',x.punto_x_di_applicazione,x.baricentrototalex,x.Aangolo_grad,x.punto_y_di_applicazione,x.baricentrototaley,x.Aangolo_grad,x.punto_eee_di_applicazione);
fprintf(aa,'nii=-(%6.3f-%6.3f)sin(%6.3f)+(%6.3f-%6.3f)cos(%6.3f)=%6.3f\n',x.punto_x_di_applicazione,x.baricentrototalex,x.Aangolo_grad,x.punto_y_di_applicazione,x.baricentrototaley,x.Aangolo_grad,x.punto_nii_di_applicazione);
fprintf(aa,'[eee,nii]=[%6.3f,%6.3f]\n\n',x.punto_eee_di_applicazione,x.punto_nii_di_applicazione);

fprintf(aa,'Asse Neutro\n');
fprintf(aa,'1+(%6.3f/%6.3f)nii+(%6.3f/%6.3f)eee=0\n',x.punto_nii_di_applicazione,x.rhoeee,x.punto_eee_di_applicazione,x.rhonii);
fprintf(aa,'[nii=%6.3feee+(%6.3f)]\n\n\n',x.m,x.quella);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	if x.sigmadelpuntopiulontano1>x.sigmadelpuntopiulontano2
	fprintf(aa,'le coordinate del punto di sforzo maggiore positivo:\n');
	elseif x.sigmadelpuntopiulontano1<x.sigmadelpuntopiulontano2
	fprintf(aa,'le coordinate del punto di sforzo maggiore negativo:\n');
	end

fprintf(aa,'[xxx,yyy]=[%6.3f,%6.3f]\n',x.puntopiulontanoxxx1,x.puntopiulontanoyyy1);
fprintf(aa,'eee=(%6.3f-%6.3f)cos(%6.3f)+(%6.3f-%6.3f)sin(%6.3f)=%6.3f\n',x.puntopiulontanoxxx1,x.baricentrototalex,x.Aangolo_grad,x.puntopiulontanoyyy1,x.baricentrototaley,x.Aangolo_grad,x.puntopiulontanoeee1);
fprintf(aa,'nii=-(%6.3f-%6.3f)sin(%6.3f)+(%6.3f-%6.3f)cos(%6.3f)=%6.3f\n',x.puntopiulontanoxxx1,x.baricentrototalex,x.Aangolo_grad,x.puntopiulontanoyyy1,x.baricentrototaley,x.Aangolo_grad,x.puntopiulontanonii1);
fprintf(aa,'[eee,nii]=[%6.3f,%6.3f] \n \n',x.puntopiulontanoeee1,x.puntopiulontanonii1);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	if x.sigmadelpuntopiulontano1>x.sigmadelpuntopiulontano2
	fprintf(aa,'le coordinate del punto di sforzo maggiore negativo:\n');
	elseif x.sigmadelpuntopiulontano1<x.sigmadelpuntopiulontano2
	fprintf(aa,'le coordinate del punto di sforzo maggiore positivo:\n');
	end

fprintf(aa,'[xxx,yyy]=[%6.3f,%6.3f]\n',x.puntopiulontanoxxx2,x.puntopiulontanoyyy2);
fprintf(aa,'eee=(%6.3f-%6.3f)cos(%6.3f)+(%6.3f-%6.3f)sin(%6.3f)=%6.3f\n',x.puntopiulontanoxxx2,x.baricentrototalex,x.Aangolo_grad,x.puntopiulontanoyyy2,x.baricentrototaley,x.Aangolo_grad,x.puntopiulontanoeee2);
fprintf(aa,'nii=-(%6.3f-%6.3f)sin(%6.3f)+(%6.3f-%6.3f)cos(%6.3f)=%6.3f\n',x.puntopiulontanoxxx2,x.baricentrototalex,x.Aangolo_grad,x.puntopiulontanoyyy2,x.baricentrototaley,x.Aangolo_grad,x.puntopiulontanonii2);
fprintf(aa,'[eee,nii]=[%6.3f,%6.3f]\n\n',x.puntopiulontanoeee2,x.puntopiulontanonii2);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	%stampa degli sforzi
	if x.sigmadelpuntopiulontano1>x.sigmadelpuntopiulontano2
	fprintf(aa,'sforzo maggiore positivo:\n');
	elseif x.sigmadelpuntopiulontano1<x.sigmadelpuntopiulontano2
	fprintf(aa,'sforzo maggiore negativo:\n');
	end
	fprintf(aa,'=(%6.3f/%6.3f)*[1+(%6.3f/%6.3f)*(%6.3f)+(%6.3f/%6.3f)*(%6.3f)]=\n',x.trazioneocompressione*x.sforzonormale,x.areatotale,x.punto_nii_di_applicazione,x.rhoeee,x.puntopiulontanonii1,x.punto_eee_di_applicazione,x.rhonii,x.puntopiulontanoeee1);
	fprintf(aa,'=%6.3f*(1+(%6.3f)+(%6.3f))=%6.3f\n',x.termine1,x.termine2,x.termine3,x.sigmadelpuntopiulontano1);

	if x.sigmadelpuntopiulontano1>x.sigmadelpuntopiulontano2
	fprintf(aa,'sforzo maggiore negativo:\n');
	elseif x.sigmadelpuntopiulontano1<x.sigmadelpuntopiulontano2
	fprintf(aa,'sforzo maggiore positivo:\n');
	end
	fprintf(aa,'=(%6.3f/%6.3f)*[1+(%6.3f/%6.3f)*(%6.3f)+(%6.3f/%6.3f)*(%6.3f)]=\n',x.trazioneocompressione*x.sforzonormale,x.areatotale,x.punto_nii_di_applicazione,x.rhoeee,x.puntopiulontanonii2,x.punto_eee_di_applicazione,x.rhonii,x.puntopiulontanoeee2);
	fprintf(aa,'=%6.3f*[1+(%6.3f)+(%6.3f)]=%6.3f\n',x.termine1,x.termine4,x.termine5,x.sigmadelpuntopiulontano2);
	
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


	
	
		if x.sigmadelpuntopiulontano1>x.sigmadelpuntopiulontano2
	fprintf(aa,'sforzo maggiore positivo:\n');
	fprintf(aa,'tresca\t\t=[(%6.3f^2)+4*(%6.3f^2)]^0.5=%6.3f\n',x.sigmadelpuntopiulontano1,x.tau,x.tresca(1,1));
	fprintf(aa,'mises\t\t=[(%6.3f^2)+3*(%6.3f^2)]^0.5=%6.3f\n',x.sigmadelpuntopiulontano1,x.tau,x.mises(1,1));
	fprintf(aa,'sforzo maggiore negativo:\n');
	fprintf(aa,'tresca\t\t=[(%6.3f^2)+4*(%6.3f^2)]^0.5=%6.3f\n',x.sigmadelpuntopiulontano2,x.tau,x.tresca(1,2));
	fprintf(aa,'mises\t\t=[(%6.3f^2)+3*(%6.3f^2)]^0.5=%6.3f\n',x.sigmadelpuntopiulontano2,x.tau,x.mises(1,2));
	elseif x.sigmadelpuntopiulontano1<x.sigmadelpuntopiulontano2
	fprintf(aa,'sforzo maggiore negativo:\n');
	fprintf(aa,'tresca\t\t=[(%6.3f^2)+4*(%6.3f^2)]^0.5=%6.3f\n',x.sigmadelpuntopiulontano1,x.tau,x.tresca(1,1));
	fprintf(aa,'mises\t\t=[(%6.3f^2)+3*(%6.3f^2)]^0.5=%6.3f\n',x.sigmadelpuntopiulontano1,x.tau,x.mises(1,1));
	fprintf(aa,'sforzo maggiore positivo:\n');
	fprintf(aa,'tresca\t\t=[(%6.3f^2)+4*(%6.3f^2)]^0.5=%6.3f\n',x.sigmadelpuntopiulontano2,x.tau,x.tresca(1,2));
	fprintf(aa,'mises\t\t=[(%6.3f^2)+3*(%6.3f^2)]^0.5=%6.3f\n',x.sigmadelpuntopiulontano2,x.tau,x.mises(1,2));
	end
	fprintf(aa,'\nla sigma massima di progetto=%6.3f\n\n',x.sigmamassimadiprogetto);



	if  x.sigmamassimadiprogetto>max(x.tresca(1,1),x.mises(1,1))
	fprintf(aa,'Quella sezione resiste a Tresca\n');
	elseif x.sigmamassimadiprogetto<max(x.tresca(1,2),x.mises(1,2))
	fprintf(aa,'Quella sezione non resiste a Tresca\n');
	end



fclose (aa);
cd ..
end