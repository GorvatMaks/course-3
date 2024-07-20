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

    def cameraBind(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setPos((0,0,10.5))
        self.cameraOn = True
        
    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(pos[0], pos[1], pos[2])
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False