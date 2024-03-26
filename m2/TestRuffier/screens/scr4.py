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



class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

        istruk3 = Label(text=txt_test3)
        
        rezult_2 = Label(text="Результат")
        rezult_vidp = Label(text="Результат після відпочинуку")

        self.rezult_2_input = TextInput(text="31", multiline=False, size_hint=(None,None) ,size=(250,30))
        self.rezult_2_input.pos_hint = {'x': 1.0, 'y': 0.5,}

        self.rezult_vidp_input = TextInput(text="28", multiline=False, size_hint=(None,None) ,size=(250,30))
        self.rezult_vidp_input.pos_hint = {'x': 1.0, 'y': 0.5,}
        
        btn = Button(text="Завершити", size_hint=(None, None) ,size=(350,100))
        btn.pos_hint = {'center_x':0.5,'center_y':0.5,}
        
        btn.on_press = self.next

        Leat_ver1 = BoxLayout(orientation="vertical")
        Leat_gor1 = BoxLayout()
        Leat_gor2 = BoxLayout()

        Leat_gor1.add_widget(rezult_2)
        Leat_gor1.add_widget(self.rezult_2_input)

        Leat_gor2.add_widget(rezult_vidp)
        Leat_gor2.add_widget(self.rezult_vidp_input)
        
        Leat_ver1.add_widget(istruk3)
        Leat_ver1.add_widget(Leat_gor1)
        Leat_ver1.add_widget(Leat_gor2)
        Leat_ver1.add_widget(btn)

        self.add_widget(Leat_ver1)
    
    def next(self):
        self.manager.current = "scr5"
        self.manager.transition.direction = "right"