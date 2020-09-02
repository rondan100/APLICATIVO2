from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np

from kivymd.app import MDApp



## Here for providing colour to the background  
from kivy.core.window import Window 

## Setting the window size 
Window.clearcolor = (1, 1, 1, 1) # White background
Window.size = (350, 650)


kv = """
#:import SlideTransition kivy.uix.screenmanager.SlideTransition

<Manager>:
    transition: SlideTransition()

    StartPage:
        name: 'StartPage'

    SecondPage:
        name: 'SecondPage'

<StartPage>:

    canvas:

        Color:
            rgba: 0.1, 0.1, 1, 0.7

        Rectangle:
            pos: 0, 11*root.height/12
            size: root.width, root.height/12

        Rectangle:
            pos: 0, 0
            size: root.width, root.height/12


    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height


    Button:
        size_hint: 0.15, 0.08
        pos_hint: {'left': 0, 'top': 1 }
        text: 'Go to Second Page'
        on_release:
            root.manager.current = 'SecondPage'

    Button:
        size_hint: 0.15, 0.08
        pos_hint: {'right': 1, 'bottom': 1 }
        text: 'Quit'
        on_release: app.stop()


    Label:
        text: 'Start Screen'
        font_size: '20sp'
        color: 0,0,0,1
        pos_hint:{'x': 0.42, 'y': 0.46 }



<SecondPage>:
    box: box

    # canvas.before:
    #     Color:
    #         rgba: 1, 1, 1, 1
    #     Rectangle:
    #         pos: self.pos
    #         size: self.size

    BoxLayout:
        id: box
        size_hint: 0.8, 0.75
        pos_hint:{'x': 0.15, 'y': 0.1 }

    # orientation: "vertical"
    # MyFigure:
    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: False

    Button:
        text:'Start Menu'
        font_size: 20
        bold: True
        size_hint: 0.15, 0.08
        pos_hint: {'left': 0, 'top': 1 }
        color: 1, 1, 1, 1
        on_press: root.manager.current = 'StartPage'

    Button:
        text:'Update'
        font_size: 20
        bold: True
        size_hint: 0.15, 0.08
        pos_hint: {'x':0.8, 'y': 0.5 }
        color: 1, 1, 1, 1
        on_press: root.Update()

    Button:
        text:'Limpar'
        font_size: 20
        bold: True
        size_hint: 0.15, 0.08
        pos_hint: {'x':0.8, 'y': 0.4 }
        color: 1, 1, 1, 1
        on_press: root.Limpar()
"""

Builder.load_string(kv)

# Start Page
class StartPage(Screen):      
    pass

#Second Page
class SecondPage(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        phase = np.random.normal(-np.pi/2, +np.pi/2)
        noise = np.random.normal(0, 1, N)
        nbr = np.linspace(0,1,N)
        func = 0.01*noise+np.sin(nbr/0.1+phase)

        plt.plot(nbr,func,label='Line1',color='r')
        plt.ylabel('Sinus')
        plt.xlabel('Range')
        plt.grid(True)
        self.fig1 = plt.gcf()

        return self.fig1

    # def on_pre_enter(self, *args):

    #     self.box.clear_widgets()

    #     self.fig1 = SecondPage.add_plot(self,1000)
    #     self.box.add_widget(FigureCanvasKivyAgg(self.fig1))

    def Update(self):
        # self.box.remove_widget(FigureCanvasKivyAgg(self.fig1))
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = SecondPage.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1,size_hint=(1,0.4),pos_hint={"top":1.2}))

    def Limpar(self):
        self.box.clear_widgets()


class Manager(ScreenManager):
    pass


class MyNewApp(MDApp):
    title = "Matplolib - plot Update"

    data = {
        "language-python": "Chess.com",
        "language-php": "LiChess",
        "language-cpp": "Chess24",
    }

    def build(self):
        return Manager()    

MyNewApp().run()