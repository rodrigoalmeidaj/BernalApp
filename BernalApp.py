from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout

class Home(ScreenManager):
    pass

class Menu(MDScreen):
    pass

class Login(MDScreen):
    pass
    
class Cadastro(MDScreen):
    pass

class TelaInicial(Screen):
    def __init__(self, atividades=[], **kwargs): #keyword arguments (poderia ser qualquer nome)
        super().__init__(**kwargs)
        for atividades in atividades:
            self.ids.box.add_widget(Funcoes(text=atividades))
            
    def addComponente(self):
        texto = self.ids.tarefa.text
        self.ids.box.add_widget(Funcoes(text=texto))
        self.ids.tarefa.text = ''
            
class Funcoes(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class BernalApp(MDApp):
    def build(self):
        self.theme_cls.theme_style= "Light"
        self.theme_cls.primary_palette = "Blue"
        return TelaInicial()

if __name__ == "__main__":
    BernalApp().run()