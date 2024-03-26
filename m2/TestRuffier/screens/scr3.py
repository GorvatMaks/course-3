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


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        istruch1 = Label(text=txt_sits)
        

        Leat_ver1 = BoxLayout(orientation="vertical")

        btn = Button(text="Продовжити", size_hint=(None, None) ,size=(350,100))
        btn.pos_hint = {'center_x':0.5,'center_y':0.5,}
        btn.on_press = self.next

        Leat_ver1 = BoxLayout(orientation="vertical")
        Leat_ver1.add_widget(istruch1)
        Leat_ver1.add_widget(btn)
        self.add_widget(Leat_ver1)

    def next(self):
        self.manager.current = "scr4"
        self.manager.transition.direction = "left"

