import kivy
kivy.require('1.9.1') # replace with your current kivy version !
############
#per installare i garden components 
#C:\Users\Von Braun\Downloads\WinPython-64bit-3.5.2.3Qt5\python-3.5.2.amd64\Scripts
#https://docs.scipy.org/doc/numpy/f2py/index.html
#!python garden install nomefile
############
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
import numpy as np
np.set_printoptions(threshold=np.nan)

#from kivy.app import App
#from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
#from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import os

#from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

"""Simple widget to display a matplolib figure in kivy"""
#from kivy.uix.widget import Widget
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backend_bases import NavigationToolbar2
from kivy.graphics.texture import Texture
from kivy.properties import ObjectProperty
from kivy.base import EventLoop
import math



from kivy.graphics import Mesh


Config.set('graphics', 'fullscreen', 1)
Window.size = (700,600)
Config.set('graphics','resizable',0)
printa=0
if printa:
    print(Window.size)
if 0:
    fullscreen=0
    if fullscreen:
        Window.size = (Window._get_width(),Window._get_height())
if printa:
    print(os.getcwd())

class LblTxt(BoxLayout):
    from kivy.properties import ObjectProperty
    theTxt = ObjectProperty(None)
"""
class CheckLista(BoxLayout):
    from kivy.uix.checkbox import CheckBox
    CheckForm = CheckBox()
"""
#https://github.com/jeysonmc/kivy_matplotlib/blob/master/README.md
#http://pythonmobile.blogspot.it/2014/06/21-checkboxes.html
class MatplotFigure(Widget):
    """Widget to show a matplotlib figure in kivy.
    The figure is rendered internally in an AGG backend then
    the rgb data is obtained and blitted into a kivy texture.
    """
    figure = ObjectProperty(None)
    _box_pos = ListProperty([0, 0])
    _box_size = ListProperty([0, 0])
    _img_texture = ObjectProperty(None)
    _bitmap = None
    _pressed = False
    figcanvas = ObjectProperty(None)
    # I Chose composition over MI because of name clashes

    def on_figure(self, obj, value):
        self.figcanvas = _FigureCanvas(self.figure, self)
        self.figcanvas._isDrawn = False
        l, b, w, h = self.figure.bbox.bounds
        #print(l,b,w,h)
        w = int(math.ceil(w))
        h = int(math.ceil(h))
        self.width = w
        self.height = h

        # Texture
        self._img_texture = Texture.create(size=(w, h))

    def __init__(self, figure=None, *args, **kwargs):
        super(MatplotFigure, self).__init__(*args, **kwargs)
        self.figure = figure
        # Event binding
        EventLoop.window.bind(mouse_pos=self.on_mouse_move)
        self.bind(size=self._onSize)

    def _draw_bitmap(self):
        if self._bitmap is None:
            print("No bitmap!")
            return
        self._img_texture = Texture.create(size=(self.bt_w, self.bt_h))
        self._img_texture.blit_buffer(
            self._bitmap, colorfmt="rgb", bufferfmt='ubyte')
        self._img_texture.flip_vertical()

    def on_mouse_move(self, window, mouse_pos):
        """ Mouse move """
        if self._pressed:  # Do not process this event if there's a touch_move
            return
        x, y = mouse_pos
        if self.collide_point(x, y):
            real_x, real_y = x - self.pos[0], y - self.pos[1]
            self.figcanvas.motion_notify_event(real_x, real_y, guiEvent=None)

    def on_touch_down(self, event):
        x, y = event.x, event.y

        if self.collide_point(x, y):
            self._pressed = True
            real_x, real_y = x - self.pos[0], y - self.pos[1]
            self.figcanvas.button_press_event(real_x, real_y, 1, guiEvent=event)

    def on_touch_move(self, event):
        """ Mouse move while pressed """
        x, y = event.x, event.y
        if self.collide_point(x, y):
            real_x, real_y = x - self.pos[0], y - self.pos[1]
            self.figcanvas.motion_notify_event(real_x, real_y, guiEvent=event)

    def on_touch_up(self, event):
        x, y = event.x, event.y
        if self._box_size[0] > 1 or self._box_size[1] > 1:
            self.reset_box()
        if self.collide_point(x, y):
            pos_x, pos_y = self.pos
            real_x, real_y = x - pos_x, y - pos_y
            self.figcanvas.button_release_event(real_x, real_y, 1, guiEvent=event)
            self._pressed = False

    def new_timer(self, *args, **kwargs):
        pass  # TODO

    def _onSize(self, o, size):
        if self.figure is None:
            return
        # Creat a new, correctly sized bitmap
        self._width, self._height = size
        self._isDrawn = False

        if self._width <= 1 or self._height <= 1:
            return

        dpival = self.figure.dpi
        winch = self._width / dpival
        hinch = self._height / dpival
        self.figure.set_size_inches(winch, hinch)
        self.figcanvas.resize_event()
        self.figcanvas.draw()

    def reset_box(self):
        self._box_size = 0, 0
        self._box_pos = 0, 0

    def draw_box(self, event, x0, y0, x1, y1):
        pos_x, pos_y = self.pos
        # Kivy coords
        y0 = pos_y + y0
        y1 = pos_y + y1
        self._box_pos = x0, y0
        self._box_size = x1 - x0, y1 - y0


class _FigureCanvas(FigureCanvasAgg):

    """Internal AGG Canvas"""

    def __init__(self, figure, widget, *args, **kwargs):
        self.widget = widget
        super(_FigureCanvas, self).__init__(figure, *args, **kwargs)
    def draw(self):
        """
        Render the figure using agg.
        """
        super(_FigureCanvas, self).draw()
        agg = self.get_renderer()
        w, h = agg.width, agg.height
        self._isDrawn = True
        self.widget.bt_w = w
        self.widget.bt_h = h
        self.widget._bitmap = agg.tostring_rgb()
        self.widget._draw_bitmap()

    def blit(self, bbox=None):
        # TODO bbox
        agg = self.get_renderer()
        w, h = agg.width, agg.height
        self.widget._bitmap = agg.tostring_rgb()
        self.widget.bt_w = w
        self.widget.bt_h = h
        self.widget._draw_bitmap()
        
    #def print_figure(self,filename, *args, **kwargs):
        #http://stackoverflow.com/questions/17538235/unable-to-save-matplotlib-figure-figure-canvas-is-none
        #http://answers.elteacher.info/questions/post/229454/plot-radec-polygons-with-astropy-wcs-aplpy-fitsfigure-ask-question.html
        #https://www.google.it/search?q=kivy+super+print_figure&ie=utf-8&oe=utf-8&client=firefox-b-ab&gfe_rd=cr&ei=jHGxWO2YK_CEygWStrPADQ
        #https://github.com/dbuscombe-usgs/lobos/blob/master/kivy_matplotlib.py
        """
        finchenonlomettiapposto=0
        if finchenonlomettiapposto:
            super(self.print_figure, self).print_figure(filename, *args, **kwargs)
            if self._isDrawn:
                self.draw()
        """


class MatplotNavToolbar(BoxLayout):

    """Figure Toolbar"""
    pan_btn = ObjectProperty(None)
    zoom_btn = ObjectProperty(None)
    home_btn = ObjectProperty(None)
    info_lbl = ObjectProperty(None)
    _navtoolbar = None  # Internal NavToolbar logic
    figure_widget = ObjectProperty(None)

    def __init__(self, figure_widget=None, *args, **kwargs):
        super(MatplotNavToolbar, self).__init__(*args, **kwargs)
        self.figure_widget = figure_widget

    def on_figure_widget(self, obj, value):
        self.figure_widget.bind(figcanvas=self._canvas_ready)

    def _canvas_ready(self, obj, value):
        self._navtoolbar = _NavigationToolbar(value, self)
        self._navtoolbar.figure_widget = obj


class _NavigationToolbar(NavigationToolbar2):
    figure_widget = None

    def __init__(self, canvas, widget):
        self.widget = widget
        super(_NavigationToolbar, self).__init__(canvas)

    def _init_toolbar(self):
        self.widget.home_btn.bind(on_press=self.home)
        self.widget.bind(on_press=self.pan)
        self.widget.zoom_btn.bind(on_press=self.zoom)

    def dynamic_update(self):
        self.canvas.draw()

    def draw_rubberband(self, event, x0, y0, x1, y1):
        self.figure_widget.draw_box(event, x0, y0, x1, y1)

    def set_message(self, s):
        self.widget.info_lbl.text = s

class LoadDialog(BoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveDialog(BoxLayout):
    save = ObjectProperty(None)
    cancel = ObjectProperty(None)

Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)
Factory.register('MatplotFigure', cls=MatplotFigure)
Factory.register('MatplotNavToolbar', cls=MatplotNavToolbar)

if __name__ == '__main__':
    # Example
    import matplotlib as mpl
    import numpy as np
    class CalcolatriceApp(App):
        ##########################################################################
        loadfile = ObjectProperty(None)
        savefile = ObjectProperty(None)
        text_input = ObjectProperty(None)

        
        
        def build_mesh(self):
            from math import sin, cos, pi
            """ returns a Mesh of a rough circle. """
            vertices = []
            indices = []
            step = 10
            istep = (pi * 2) / float(step)
            for i in range(step):
                x = 300 + cos(istep * i) * 100
                y = 300 + sin(istep * i) * 100
                vertices.extend([x, y, 0, 0])
                indices.append(i)
            """
            Mesh:
                vertices: (x1, y1, s1, v1, x2, y2, s2, v2, x3, y3, s3, v3...)
                indices: (1, 2, 3...)
                texture: some_texture
                rgba: 1,1,1,1
                mode: some_mode
                """
            #ritorna una area colorata chiusa
            return Mesh(vertices=vertices, indices=indices, mode='triangle_fan')
            #return Mesh(vertices=vertices, indices=indices, mode='line_loop')

        def dismiss_popup(self):
            self._popup.dismiss()
    
        def show_load(self):
            content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
            self._popup = Popup(title="Carica File", content=content,
                                size_hint=(0.9, 0.9))
            self._popup.open()
    
        def show_save(self):
            content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
            self._popup = Popup(title="Salva File", content=content,
                                size_hint=(0.9, 0.9))
            self._popup.open()
    
        def load(self, path, filename):
            self.stringa=np.asmatrix(np.genfromtxt(os.path.join(path, filename[0]),delimiter=","))
            print(self.stringa)
            print(filename)
            self.vada=np.size(self.stringa,0)-1
            #print(self.vada)
            self.root.ids.nomArch.theTxt.text=filename[0]
            fig = mpl.figure.Figure(figsize=(self.mmma, self.mmmb))
            axes = fig.gca()
            from calcolatrice.stampafigura import disegna
            disegna(self,self.stringa)
            figure_wgt = self.root.ids['figure_wgt']  # MatplotFigure
            figure_wgt.figure = fig

            #with open(os.path.join(path, filename[0])) as stream:
                #self.text_input.text = stream.read()
            self.dismiss_popup()
    
        def save(self, path, filename):
            #with open(, 'w') as stream:
            nome=self.root.ids.nomArch.theTxt.text
            #print("dd"+nome+"dd")
            strada=os.getcwd()+"\\" + nome
            #print(os.getcwd())
            #print(os.path.join(path, filename[0]))
            #stream.write(self.stringa)
            #print(strada)
            np.savetxt(strada, self.stringa, delimiter=',', newline='\n')    
            self.dismiss_popup()
        def salvaauto(self,*args):
            if self.vada>0:
                nome=self.root.ids.nomArch.theTxt.text
                estensione=".csv"
                strada=os.getcwd()+"\\" + nome
                nomeTemp=nome
                if nome=="":
                    k=0
                    nomeTemp="ciccione"+"0"+str(k)+str(estensione)
                    strada=os.getcwd()+"\\"+nomeTemp
                    while os.path.isfile(strada)==True:
                        nomeTemp="ciccione"+"0"+str(k)+str(estensione)
                        strada=os.getcwd()+"\\"+nomeTemp
                        k=k+1
                #print(strada)
                np.savetxt(strada, self.stringa, delimiter=',', newline='\n')    
                self.root.ids.nomArch.theTxt.text=nomeTemp
        ##########################################################################
        title = "Disegnatore di Biancardi"
        #stringa= MatrixProperty()
        #Status=StringProperty()
        def UndoZZZZ(self,*args):
            if self.vada>0:
                self.vada=self.vada-1
                self.stringa=self.stringa[:-1,:]
                fig = mpl.figure.Figure(figsize=(self.mmma, self.mmmb))
                axes = fig.gca()
                figure_wgt = self.root.ids['figure_wgt']  # MatplotFigure
                figure_wgt.figure = fig
                from calcolatrice.stampafigura import disegna
                disegna(self,self.stringa)
                self.root.ids.risoluzione.text="figure inserite %d"%self.vada

            #self.stringa=np.matrix("42015.,3.,1.,48.,0.,0.,0.,0.,0.,0.,0.;4.,1.,0.,0.,0.,0.,6.,10.,6.,10.,0.;2.,-1.,0.,4.,0.,3.,0.,3.1415,0.,0.,0.")
        def Resetta(self,*args):
            if self.vada>0:
                self.stringa=self.iniziale
                #self.root.ids.schifo.text=print(self.stringa)
                #print(self.stringa)
                self.vada=0
                #self.root.ids.schifo.text=""
                self.root.ids.risoluzione.text="resettato"
                fig = mpl.figure.Figure(figsize=(self.mmma, self.mmmb))
                fig.clf()
                figure_wgt = self.root.ids['figure_wgt']  # MatplotFigure
                figure_wgt.figure = fig
                self.root.ids.risoluzione.text="figure inserite %d"%self.vada

        def SalvaDisegno(self,*args):
            if self.vada>0:
                #print(self.root.ids.figure_wgt.figure.figure)
                #print(self.root.ids.figure_wgt.figure.bbox.bounds)
                #print(self.root.ids.figure_wgt.figure.dpi)
                #self.root.ids.figure_wgt.figure.savefig(filename)
                nome=self.root.ids.nomArch.theTxt.text
                estensione=".png"
                strada=os.getcwd()+"\\" + nome
                nomeTemp=nome
                if nome=="":
                    k=0
                    nomeTemp="ciccione"+"0"+str(k)+estensione
                    strada=os.getcwd()+"\\"+nomeTemp
                    while os.path.isfile(strada)==True:
                        nomeTemp="ciccione"+"0"+str(k)+estensione
                        strada=os.getcwd()+"\\"+nomeTemp
                        k=k+1
                #print(strada)
                self.root.ids.nomArch.theTxt.text=nomeTemp
                self.root.ids.figure_wgt.export_to_png(self.root.ids.nomArch.theTxt.text)
                #from matplotlib.backends.backend_pdf import PdfPages
                #with PdfPages('multipage_pdf.pdf') as pdf:
                    #pdf.savefig(self.root.ids.figure_wgt.figure)
        def BottonePremutoNocciolo(self,*args):
            if self.vuoifareancheilnocciolo==0:
                self.vuoifareancheilnocciolo=1
                self.iniziale[0,2]=1
            elif self.vuoifareancheilnocciolo==1:
                self.vuoifareancheilnocciolo=0
                self.iniziale[0,2]=0
            print('The checkbox is active')
        def build(self):
            # Matplotlib stuff, figure and plot
            fig = mpl.figure.Figure(figsize=(self.mmma, self.mmmb))
            axes = fig.gca()
            #axes.set_xlim(0, 50)
            #axes.grid(True)
            #fig.clf()
            axes.axis("on")
            #axes.set_xlim(0, 50)
            #axes.set_aspect('equal')
            # Kivy stuff
            root = Builder.load_file("nuovaForma.kv")
            figure_wgt = root.ids['figure_wgt']  # MatplotFigure
            figure_wgt.figure = fig
            self.root=root
            self.root.ids.risoluzione.text="figure inserite %d"%self.vada
            return root
        def __init__(self, **kwargs):
            super(CalcolatriceApp, self).__init__(**kwargs)
            self.mmma=2
            self.mmmb=2
            self.vada=0
            self.scalatore=1000
            self.kk=3
            self.discretizzaarchicerchi=80
            self.vuoifareancheilnocciolo=1
            self.contorna=1
            self.vuota=np.matrix("0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.")
            self.iniziale=np.matrix("0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.")
            self.iniziale[0,0]=42015.
            self.iniziale[0,1]=self.kk
            self.iniziale[0,2]=self.vuoifareancheilnocciolo
            self.iniziale[0,3]=self.discretizzaarchicerchi
            self.iniziale[0,4]=self.contorna
            self.stringa=self.iniziale
            self.vada=0
            #print(self.stringa)
        def Internet(*args):
            """
            For documentation of the webbrowser module,
            see http://docs.python.org/library/webbrowser.html
            """
            import webbrowser
            new = 2 # open in a new tab, if possible
            # open a public URL, in this case, the webbrowser docs
            url = "https://www.facebook.com/francescoscodesection\n"
            webbrowser.open(url,new=new)
            # open an HTML file on my own (Windows) computer
            #url = "file://X:/MiscDev/language_links.html"
            #webbrowser.open(url,new=new)
        def Calcolalo(self,*args):
            #import os
            #os.chdir("C:\Users\Von Braun\Google Drive\mat2pylab\calcolatrice")
            noncidevonoessereaste=1
            from calcolatrice.misuras import guardasecisonoaste
            noncidevonoessereaste=guardasecisonoaste(self)
            if noncidevonoessereaste and 0:
                self.stringa[0,2]=0
                self.vuoifareancheilnocciolo=0
            if self.vada>0:
                import time
                b0=time.clock()
                self.salvaauto(self)
                fig = mpl.figure.Figure(figsize=(self.mmma, self.mmmb))
                axes = fig.gca()
                figure_wgt = self.root.ids['figure_wgt']  # MatplotFigure
                figure_wgt.figure = fig
                #print(self.root.ids.figure_wgt.figure)
                if self.root.ids.quantidiscreti.theTxt.text!="":
                    self.stringa[0,3]=int(self.root.ids.quantidiscreti.theTxt.text)
                from calcolatrice.principale import codicesezione
                self.root.ids.risoluzione.text=codicesezione(self)
                #filename=self.root.ids.nomArch.theTxt.text
                #mpl.draw()
                #self.print_figure(self, filename)
                b=time.clock()
                print("tempo",round(b-b0,4))
                #self.uscita="cacca"+"\n"
                #self.root.ids.risoluzione.text=self.uscita
            else:
                self.root.ids.risoluzione.text="figure inserite %d"%self.vada
        def CreaSalvataggio(self,*args):
            if args[1]==1:
                val2=0. if args[2]=="" else str(args[2])
                val3=0. if args[3]=="" else str(args[3])
                val4=0. if args[4]=="" else str(args[4])
                val5=0. if args[5]=="" else str(args[5])
                if val2+val3+val4+val5!=0:
                    #val="1 "+val2+" 0 "+val3+" "+val4+" "+val5
                    from calcolatrice.misuras import UnireMatriciCol
                    self.stringa=UnireMatriciCol(self.stringa,self.vuota)
                    self.vada=self.vada+1
                    self.stringa[self.vada,0]=1.
                    self.stringa[self.vada,1]=float(val2)
                    self.stringa[self.vada,3]=float(val3)
                    self.stringa[self.vada,4]=float(val4)
                    self.stringa[self.vada,5]=float(val5)
                #print("10000",val)
                #stringa=stringa+args[1]+" "+args[2]+" "+args[3]+" "+args[4]+";"
            if args[1]==2:
                val2=0. if args[2]=="" else float(args[2])
                val3=0. if args[3]=="" else float(args[3])
                val4=0. if args[4]=="" else float(args[4])
                val5=0. if args[5]=="" else float(args[5])
                val6=0. if args[6]=="" else float(args[6])
                val7=0. if args[7]=="" else float(args[7])
                if val2+val3+val4+val5+val6+val7!=0:
                    self.vada=self.vada+1
                    #val="2 "+val2+" 0 "+val3+" "+val4+" "+val5+" "+val6+" "+val7
                    from calcolatrice.misuras import UnireMatriciColNon
                    self.stringa=UnireMatriciColNon(self.stringa,self.vuota)
                    self.stringa[self.vada,0]=2.
                    self.stringa[self.vada,1]=float(val2)
                    self.stringa[self.vada,3]=float(val3)
                    self.stringa[self.vada,4]=float(val4)
                    self.stringa[self.vada,5]=float(val5)
                    self.stringa[self.vada,6]=float(val6)*np.pi/180
                    self.stringa[self.vada,7]=float(val7)*np.pi/180

                #print("20000",val)
                #stringa=stringa+args[1]+" "+args[2]+" "+args[3]+" "+args[4]+" "+args[5]+" "+args[6]+";"
            if args[1]==2.5:
                val2=0. if args[2]=="" else str(args[2])
                val3=0. if args[3]=="" else str(args[3])
                val4=0. if args[4]=="" else str(args[4])
                val5=0. if args[5]=="" else str(args[5])
                val6=0. if args[6]=="" else str(args[6])
                val7=0. if args[7]=="" else str(args[7])
                if val2+val3+val4+val5+val6+val7!=0:
                    self.vada=self.vada+1
                    #val="2 "+val2+" 0 "+val3+" "+val4+" "+val5+" "+val6+" "+val7
                    from calcolatrice.misuras import UnireMatriciColNon
                    self.stringa=UnireMatriciColNon(self.stringa,self.vuota)
                    self.stringa[self.vada,0]=2.5
                    self.stringa[self.vada,1]=float(val2)
                    self.stringa[self.vada,3]=float(val3)
                    self.stringa[self.vada,4]=float(val4)
                    self.stringa[self.vada,5]=float(val5)
                    self.stringa[self.vada,6]=float(val6)
                    self.stringa[self.vada,7]=float(val7)
            if args[1]=="":
                inter=0
            else:
                inter=int(args[1])
            if printa:
                print("inter",inter)
            if inter>=3:
                #print(*args)
                #print(args[0])
                #print(args[1])
                #print(args[2])
                #print(args[3])
                val1=0. if args[1]=="" else float(args[1])
                val2=0. if args[2]=="" else float(args[2])
                val3=0. if args[3]=="" else str(args[3])
                from calcolatrice.misuras import UnireMatriciCol,UnireMatriciRig
                self.vada=self.vada+1
                #val=val1 +" "+val2+" 0 "+val3
                from calcolatrice.misuras import StringaToMatrix
                val4=StringaToMatrix(val3)
                if np.size(val4)==2*val1:
                    print("ok")
                else:
                    val1=np.size(val4)
                    print("non sono giuste")
                    #self.root.ids.n
                val5=np.matrix("0. 0. 0.")
                val5[0,0]=float(val1)
                val5[0,1]=float(val2)
                #print(val4)
                val6=UnireMatriciRig(val5,val4)
                #self.stringa[self.vada,3]=float(val3)
                #print(val6,type(val6))
                from calcolatrice.misuras import UnireMatriciColNon
                self.stringa=UnireMatriciColNon(self.stringa,val6)
                #if printa:
            #print(self.stringa)
            #print("30000",val)
            #print("fine",self.stringa)
            #self.stringa=self.stringa+val+";"
            #print("finish  ",self.stxringa)
            fig = mpl.figure.Figure(figsize=(self.mmma, self.mmmb))
            axes = fig.gca()
            figure_wgt = self.root.ids['figure_wgt']  # MatplotFigure
            figure_wgt.figure = fig
            from calcolatrice.stampafigura import disegna
            disegna(self,self.stringa)
            self.root.ids.risoluzione.text="figure inserite %d"%self.vada
            #mpl.savefig("ciccio.png")

            #stampa=self.stringa
            #self.root.ids.schifo.text="booooooooh"
            #self.root.ids.schifo.text=print(stampa)
            #str.replace(stampa,";",";\n")
            #disegna(self,numero1,kk,discretizzaarchicerchi)
            return self
    CalcolatriceApp().run()

"""
There are three keywords specific to Kv language:
app: always refers to the instance of your application.
root: refers to the base widget/template in the current rule
self: always refer to the current widget
"""
#print(Window._get_width())
#print(Window._get_height())
    #Builder.unload_file(root,file1)
    #Builder._clear_matchcache(self)
    #unbind_property(self, widget, name)
#password=True
#multiline=False   


#pulsante salva disegno
#pulsante leggi file esterno
#pulsante leggi dxf
#pulsante salva file
#press the row under here to cast another kv file
#":include load.kv"