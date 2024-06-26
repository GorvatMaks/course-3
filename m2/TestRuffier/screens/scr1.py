from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction,txt_test1, txt_test2, txt_test3, txt_sits
from rufier import test
from utils2 import*


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

        istruk = Label(text=txt_instruction,bold = True,
                              font_size="20sp",color=(0.055, 0.235, 0.541, 1))
        istruk.bind(width=lambda *x: istruk.setter('text_size')(istruk, (istruk.width, None)))
        istruk.bind(texture_size=lambda *x: istruk.setter('height')(istruk, istruk.texture_size[1]))
        
        name = Label(text="Введіть ім'я",bold = True,
                              font_size="20sp",
                              pos_hint={'center_x': 0.5, 'center_y': .85},
                              size_hint=(None, None),
                              halign="center",
                              color=(0.055, 0.235, 0.541, 1))
        
        old = Label(text="Введіть вік",bold = True,
                              font_size="20sp",
                              pos_hint={'center_x': 0.5, 'center_y': .85},
                              size_hint=(None, None),
                              halign="center",
                              color=(0.055, 0.235, 0.541, 1))



    
        self.name_input = TextInput(text="Максон", multiline=False, size_hint=(None,None) ,size=(250,30), halign="center")
        self.name_input.pos_hint = {'x': 1.0, 'y': 0.5,}

        self.old_input = TextInput(text="15", multiline=False, size_hint=(None,None) ,size=(250,30), halign="center")
        self.old_input.pos_hint = {'x': 1.0, 'y': 0.5,}


        btn = Button(text="Почати", size_hint=(None, None) ,size=(350,100))
        btn.pos_hint = {'center_x':0.5,'center_y':0.5,}
        
        btn.on_press = self.next
        
        Leat_ver1 = BoxLayout(orientation="vertical")
        Leat_gor1 = BoxLayout()
        Leat_gor2 = BoxLayout()

        Leat_gor1.add_widget(name)

        Leat_gor1.add_widget(self.name_input)

        Leat_gor2.add_widget(old)
        Leat_gor2.add_widget(self.old_input)
        
        Leat_ver1.add_widget(istruk)
        Leat_ver1.add_widget(Leat_gor1)
        Leat_ver1.add_widget(Leat_gor2)
        Leat_ver1.add_widget(btn)

        self.add_widget(Leat_ver1)

    def next(self):
        name = self.name_input.text
        age = self.old_input.text
        self.manager.current = "scr2"
        self.manager.transition.direction = "right"
        rid = rFile()
        rid["name"] = name
        rid["age"] = age
        wFile(rid)
        

