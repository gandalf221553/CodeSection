def RowChanger(row,textToSearch,textToReplace,fileToSearch):
    a=1
    import fileinput
    tempFile = open( fileToSearch, 'r+' )
    for line in fileinput.input( fileToSearch ):
        if row in line :
            print('done yet')
            a=0
    if a:
        if textToReplace=="0":
            textToReplace = textToSearch+"\n"+row
        #fileToSearch = 'D:\dummy1.txt'
        tempFile = open( fileToSearch, 'r+' )
        for line in fileinput.input( fileToSearch ):
            if textToSearch in line :
                print('done now')
            tempFile.write(line.replace(textToSearch,textToReplace))
        tempFile.close()
#http://pythoncentral.io/pyinstaller-package-python-applications-windows-mac-linux/
def ModSpec():
    print("modddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
    import os
    print(os.path.basename(os.path.dirname(os.path.realpath(__file__))))
    #nome=os.path.basename(os.path.dirname(os.path.realpath(__file__)))
    nome="kivy_matplotlib"
    icon=1
    onefile=0
    executive=0
    vuoimettereunimmagine=0
    altrecartelle=0
    versionfile=0
    nomepy=nome+".py"
    nomespec=nome+".spec"
    nomecart="\\"+nome+"\\"
    nomeIcon="icon.ico"
    
    import platform
    #windowsonly="" if StringCnf(platform.system(),"Windows") else  windowsonly=" -m "
    from calcolatrice.misuras import StringCnf
    if StringCnf(platform.system(),"Windows"):
        windowsonly=" -m "
    else:
        windowsonly=""
    if onefile:
        vuoifareunfile=" --onefile"
    else:
        vuoifareunfile=""
    if vuoimettereunimmagine:
        nomeimmagine="logo.png"
    else:
        nomeimmagine=""
    
    if icon:
        iconStr=" --icon "+nomeIcon+" "
    else:
        iconStr=""
    #compilatore
    a=""#"\\"+os.getcwd()
    
    posizione=a+nomepy
    
    if versionfile:
        versionfile=" --version-file=version.txt "
    else:
        versionfile=""
    
    pythonpath="!python "#"C:\\Users\\Von Braun\\Downloads\\WinPython-64bit-3.5.2.3Qt5\\python-3.5.2.amd64\\Scripts\\pyinstaller.exe  "
    #pythonpath="path='"+a+"'"
    #pythonpath=     "C:\Users\Von Braun\Downloads\WinPython-64bit-3.5.2.3Qt5\python-3.5.2.amd64\python.exe "
    pyinstallerpath="PyInstaller "
    #pyinstallerpath="C:\Users\Von Braun\Downloads\WinPython-64bit-3.5.2.3Qt5\python-3.5.2.amd64\Lib\site-packages\PyInstaller\building\makespec.py "
    #http://stackoverflow.com/questions/8663046/how-to-install-a-python-package-from-within-ipython
    #%%!python -m PyInstaller --onefile --name nome --icon icon.ico kivy_matplotlib.py
    print("\n\n ATTENDI.....POTRESTI DOVER ASPETTARE MOLTO TEMPO\n\n")
    creaspecfile=pythonpath+windowsonly+pyinstallerpath+posizione+vuoifareunfile+" --windowed "+"  --name "+nome+iconStr+versionfile
    print(creaspecfile)
    print("\n\n")
    if executive and 0:
        #from IPython import get_ipython
        #ipython = get_ipython()
        #ipython.magic(exec(creaspecfile)) 
        #run(creaspecfile)
        #exec(input("inserisci la frase di sopra\n\n"))
        import PyInstaller.__main__
        specpath="--specpath " +os.getcwd()           #/opt/bk/spec
        distpath="--distpath " +os.getcwd()+"\\dist"  #/opt/bk/dist
        workpath="--workpath " +os.getcwd()+"\\build" #/opt/bk/build
        print(specpath)
        print(distpath)
        print(workpath)
        #import PyInstaller.utils.cliutils.makespec
        #'C:\\Users\\Von Braun\\Google Drive\\mat2pylab\\ProgettoTesi3.86\\hello'
        #'C:\\Users\\Von Braun\\Downloads\\WinPython-64bit-3.5.2.3Qt5\\settings'
        #pathex=['C:\\Users\\Von Braun\\Downloads\\WinPython-64bit-3.5.2.3Qt5\\python-3.5.2.amd64\\Lib\\site-packages\\PyInstaller']
        #PyInstaller.__main__.run_makespec([nomepy,pathex])
        PyInstaller.__main__.run(["-y", "-w",nomepy])
        #exec(creaspecfile)
    if 1:
        import os.path
        esistelospec=os.path.isfile(nomespec)
        if esistelospec==0:
            from sys import exit
            exit()
    print("\ncreazione dello spec completata")
    
    #add this lines to the spec fil
    #http://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file-using-python
    print("modifica dello spec in corso\n\n")
    import fileinput
    riga="from kivy.deps import sdl2, glew"
    textToSearch = "# -*- mode: python -*-"
    NomeFile  = nome+".spec"
    #fileToSearch = 'D:\dummy1.txt'
    RowChanger(riga,textToSearch,"0",NomeFile)
    
    if altrecartelle:
        nuova="Tree('.."+nomecart+"'),"
        textToSearch="coll = COLLECT(exe,"
        textSub=textToSearch+nuova
        RowChanger(nuova,textToSearch,textSub,NomeFile)
    
    #if icona:
    #    modIcon="          "+"icon='icon.ico',"
    #    cerca="exe = EXE(pyz,"
    #    Modificatore(modIcon,cerca,"0",NomeFile)
    
    cerca2="a.datas,"
    modText2="               "+"*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],"
    RowChanger(modText2,cerca2,"0",NomeFile)
    print("spec file completed")
    print("modddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")

    #coll = COLLECT(exe, Tree('examples-path\\demo\\touchtracer\\'),
    
    #--onefile
    
    print("\n\nsta per iniziare la compilazione, attendi fino a che non avrà finito, troverai il file exe nella cartella DIST\n")
    compilaspecfile=pythonpath+windowsonly+pyinstallerpath+nomespec
    print(compilaspecfile)
    if executive:
        #ipython = get_ipython()
        #exec(input("inserisci la frase di sopra\n\n"))
        import PyInstaller.__main__
        PyInstaller.__main__.run(["-y", "-w","kivy_matplotlib.py"])

        #run(exec(creaspecfile))
    print("\ncompilation complete")
    
"""
       if args.filenames[0].endswith('.spec'):
            spec_file = args.filenames[0]
        else:
            spec_file = run_makespec(**vars(args))
        ##############################################################################################
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        a=os.getcwd()
        print(a)
        #os.chdir("C:\\Users\\Von Braun\\Google Drive\\mat2pylab\\ProgettoTesi4.00")
        print(spec_file)
        from compilatore import ModSpec
        ModSpec()
        os.chdir(a)
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        ##############################################################################################
        run_build(pyi_config, spec_file, **vars(args))
"""