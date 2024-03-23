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
from screens import scr1,scr2,scr3,scr4,scr5
age = 7
name = ""
p1, p2, p3 = 0, 0, 0


class Myapp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(scr1.FirstScreen(name="scr1"))
        sm.add_widget(scr2.SecondScreen(name="scr2"))
        #sm.current = "scr2"
        return sm

app = Myapp()
app.run()    