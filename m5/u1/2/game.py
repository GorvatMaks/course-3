# напиши тут код основного вікна гри
from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = MapManager()
        base.camLens.setFov(90)



base = Game()
base.run()