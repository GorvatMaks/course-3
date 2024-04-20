from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from rufier import test
from utils2 import*


class FaifScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ret = rFile()
        res = ret["Ruffrezult"]
        
        
        istruk5 = Label(text=(f"І'мя {ret['name']}"))
        istruk12 = Label(text=(f"{res}"))
    

        ver = BoxLayout(orientation="vertical")


        ver.add_widget(istruk5)
        ver.add_widget(istruk12)

        self.add_widget(ver)