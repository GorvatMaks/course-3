# напиши свій код тут

class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.model = "flamingo"
        self.hero = loader.loadModel(self.model)
        self.hero.setColor(1,1,0)
        self.hero.setScale(0.05)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.acceptEvents()

    def cameraBind(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setPos((0,0,10.5))
        self.cameraOn = True
        
    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def acceptEvents(self):
        base.accept("c", self.changeView)
        base.accept("n", self.povortLeft)
        base.accept("m", self.povorotRight)
        base.accept("n" + "-repeat", self.povortLeft)
        base.accept("m" + "-repeat", self.povorotRight)

    def povortLeft(self):
        self.hero.setH((self.hero.getH() + 5)%360)
    
    def povorotRight(self):
        self.hero.setH((self.hero.getH() - 5)%360)