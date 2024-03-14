from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class Myapp(App):
    def build(self):
        but = Button(text="Батон", color = "yellow")
        but2 = Button(text="Батон", color = "red")
        but3 = Button(text="Батон", color = "green")
        but4 = Button(text="Батон", color = "blue")
        
        lay = Label(text="не Батон")
        leayt = BoxLayout()
        leayt2 = BoxLayout()
        layout = BoxLayout(orientation="vertical")
        layout2 = BoxLayout(orientation="vertical")
        layout.add_widget(but2)
        layout.add_widget(but)
        leayt.add_widget(layout)
        leayt.add_widget(layout2)
        layout2.add_widget(leayt2)
        leayt2.add_widget(but3)
        leayt2.add_widget(but4)
        layout2.add_widget(lay)



        

        return leayt


appp = Myapp()

appp.run()