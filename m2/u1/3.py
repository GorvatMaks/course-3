from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class Myapp(App):
    def build(self):
        but = Button(text="Батон", color = "yellow")
        but2 = Button(text="Батон", color = "yellow")
        
        lay = Label(text="не Батон")
        leayt = BoxLayout()
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(but2)
        layout.add_widget(but)
        leayt.add_widget(layout)
        leayt.add_widget(lay)


        

        return leayt


appp = Myapp()

appp.run()