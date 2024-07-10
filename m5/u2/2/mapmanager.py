# напиши тут код створення та управління карткою
class MapManager():
    def __init__(self):
        self.model = "block.egg"
        self.modelTexture = "block.png"
        self.color = (0,0,1,0.5)
        self.startnew()

    def addblock(self,pos):
        self.block = loader.loadModel(self.model)
        self.blockTexture = loader.loadTexture(self.modelTexture)
        self.block.setTexture(self.blockTexture)
        self.block.setPos(pos)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
    
    def startnew(self):
        self.land = render.attachNewNode("Land")

    def addland(self, filename):
        with open(filename) as file:
            y = 0
            for radok in file:
                x = 0 
                radok_split = radok.split(" ")                
                for sumvol in radok_split:
                    for vusota in range(int(sumvol)+1):
                        
                        self.addblock((x,y,vusota))
                    x = x + 1
                y = y + 1                
                    