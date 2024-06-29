# напиши здесь код создания и управления картой

class MapManager():
    def __init__(self):
        self.model = "block.egg"
        self.modelTexture = "block.png"
        self.color = (0,0,1,0.5)
        self.startnew()
        self.addblock((1,4,1))    
        self.addblock((0,4,-1))    

    def addblock(self,pos):
        self.block = loader.loadModel(self.model)
        self.blockTexture = loader.loadTexture(self.modelTexture)
        self.block.setTexture(self.blockTexture)
        self.block.setPos(pos)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
    
    def startnew(self):
        self.land = render.attachNewNode("Land")
