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


        self.istruk5 = Label(text='')
        self.istruk12 = Label(text='')

        ver = BoxLayout(orientation="vertical")

        ver.add_widget(self.istruk5)
        ver.add_widget(self.istruk12)

        self.add_widget(ver)

    def on_enter(self):
        ret = rFile()
        res = ret["Ruffrezult"]
        self.istruk5.text = f"І'мя {ret['name']}"
        self.istruk12.text = f"{res}"