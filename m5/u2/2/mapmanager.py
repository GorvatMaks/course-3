import pickle


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
        
    def delblock(self, pos):
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()

    def buildblock(self, pos):
        x,y,z = pos
        new = self.findHighestEmpy(pos)
        
        if new[2] <= z+1:
            self.addblock(new)
        
    def delblockfrom(self, pos):    
        x,y,z = self.findHighestEmpy(pos)
        
        kordn = x,y,z-1
        self.delblock(kordn)

    def saveMap(self):
        block = self.land.getChildren()
        with open ("mymap.dat", "wb") as f:
            pickle.dump(len(block), f)  
           
            for b in block:
                x,y,z = b.getPos()
                pos =(int(x),int(y),int(z))
                pickle.dump(pos, f)

    def loadMap(self):
        pass