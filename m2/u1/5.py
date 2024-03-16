from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager


class FirstScreen(Screen):
    def __init__(self, name):
        super().__init__(name = name)

        btn = Button(text="інший скрін",color="red")
        self.add_widget(btn)
        btn.on_press = self.next
    
    def next(self):
        self.manager.current = "scr2"
        self.manager.transition.direction = "left"



class SecondScreen(Screen):
    def __init__(self, name):
        super().__init__(name = name)

        btn = Button(text="скрін 2", color="green")
        self.add_widget(btn)

        btn.on_press = self.next

    def next(self):
        self.manager.current = "scr1"
        self.manager.transition.direction = "up"

class Myapp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name="scr1"))
        sm.add_widget(SecondScreen(name="scr2"))
        #sm.current = "scr2"
        return sm

app = Myapp()
app.run()    