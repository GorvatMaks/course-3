# напиши тут код основного вікна гри
from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = MapManager()
        x, y = self.land.addland("m5/u2/2/land2.txt") 
        base.camLens.setFov(90)
        
        self.hero = Hero((x//2, y//2, 2), self.land)
        


base = Game()
base.run()
