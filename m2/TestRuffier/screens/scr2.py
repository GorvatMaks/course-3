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



class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        istruch = Label(text=txt_test1)
        
        rezult = Label(text="Введіть Результат")


        self.rezult_input = TextInput(text="73", multiline=False, size_hint=(1, 0.11) ,size=(50,30))
        self.rezult_input.pos_hint = {'x': 1.0, 'y': 0.5,}

        btn = Button(text="Продовжити", size_hint=(None, None) ,size=(350,100))
        btn.pos_hint = {'center_x':0.5,'center_y':0.5,}
        btn.on_press = self.next
        
        Leat_ver1 = BoxLayout(orientation="vertical")

        Leat_gor1 = BoxLayout()

        Leat_ver1.add_widget(istruch)
        
        Leat_gor1.add_widget(rezult)
        Leat_gor1.add_widget(self.rezult_input)

        Leat_ver1.add_widget(Leat_gor1)
        Leat_ver1.add_widget(btn)

        self.add_widget(Leat_ver1)
    
    def next(self):
        rezult = self.rezult_input.text
        self.manager.current = "scr3"
        self.manager.transition.direction = "left"
        rid = rFile()
        rid["p1"] = rezult
        wFile(rid)

