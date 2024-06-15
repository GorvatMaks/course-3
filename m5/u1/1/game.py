from direct.showbase.ShowBase import ShowBase


class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.model = loader.loadModel("m5/u1/2/block.egg")
        self.model.reparentTo(render)
        base.camLens.setFov(90)
        self.model.setPos(0,100,-5)
        self.model.setScale(0.1)


base = Game()
base.run()