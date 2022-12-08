from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
import plyer

class Home(ScreenManager):
    pass

class HomeMenu(MDScreen):
    pass

class Login(MDScreen):
    pass
    
class Cadastro(MDScreen):
    pass

class MenuApp(MDScreen):
    pass

class Anotacoes(MDScreen):
    def __init__(self, atividades=[], **kwargs):
        super().__init__(**kwargs)
        for atividades in atividades:
            self.ids.boxNotes.add_widget(Funcoes(text=atividades))
            
    def addComponente(self):
        texto = self.ids.notePad.text
        self.ids.boxNotes.add_widget(Funcoes(text=texto))
        self.ids.notePad.text = ''
            
class Funcoes(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class BernalApp(MDApp):
    def build(self):
        self.theme_cls.theme_style= "Light"
        self.theme_cls.primary_palette = "Blue"
        return Home()
    
    def notificacao(self):
        return plyer.notification.notify(title='BernalApp', message="O App está em execução")

if __name__ == "__main__":
    BernalApp().notificacao()
    BernalApp().run()