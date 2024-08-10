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

        self.block.setTag("at",str(pos))
    
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
            return x, y 

    def findBlocks(self, pos):
        return self.land.findAllMatches("=at="+str(pos))
    
    def findHighestEmpy(self,pos):
        x, y, z = pos
        z = 1

        while not self.isEmpty((x,y,z)):
            z +=1
        return x, y, z
    
    def isEmpty(self, pos):
        allblocks = self.findBlocks(pos)
        
        if allblocks:
            return False
        else:
            return True
