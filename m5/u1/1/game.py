from direct.showbase.ShowBase import ShowBase


class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.model = loader.loadModel("sword")
        self.model.reparentTo(render)
        base.camLens.setFov(90)
        self.model.setPos(-2,25,-3)
        #self.model.setScale(0.1)


base = Game()
base.run()