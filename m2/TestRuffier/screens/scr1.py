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



class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

        istruk = Label(text=txt_instruction)
        
        name = Label(text="Введіть ім'я")
        old = Label(text="Введіть вік")

        self.name_input = TextInput(text="Максон", multiline=False)
        old_input = TextInput(text="15", multiline=False)

        btn = Button(text="Почати")
        btn.on_press = self.next
        
        Leat_ver1 = BoxLayout(orientation="vertical")
        Leat_gor1 = BoxLayout()
        Leat_gor2 = BoxLayout()

        Leat_gor1.add_widget(name)
        Leat_gor1.add_widget(self.name_input)

        Leat_gor2.add_widget(old)
        Leat_gor2.add_widget(old_input)
        
        Leat_ver1.add_widget(istruk)
        Leat_ver1.add_widget(Leat_gor1)
        Leat_ver1.add_widget(Leat_gor2)
        Leat_ver1.add_widget(btn)

        self.add_widget(Leat_ver1)

    def next(self):
        global name
        name = self.name_input.text
        #print(name)
        self.manager.current = "scr2"
        self.manager.transition.direction = "right"

