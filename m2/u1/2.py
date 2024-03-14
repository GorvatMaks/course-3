from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

def GG():
    print("Батон")

class Myapp(App):
    def build(self):
        but = Button(text="Батон", color = "yellow")
        lay = Label(text="не Батон")
        leayt = BoxLayout()
        leayt.add_widget(lay)
        leayt.add_widget(but)

        but.on_press = GG

        return leayt


appp = Myapp()

appp.run()
