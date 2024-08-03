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
        self.mode = True

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
        

        base.accept("w", self.forward)
        base.accept("s", self.back)
        base.accept("a", self.left)
        base.accept("d", self.right)
        
        base.accept("e", self.up)
        base.accept("q", self.down)

        base.accept("w" + "-repeat", self.forward)
        base.accept("s" + "-repeat", self.back)
        base.accept("a" + "-repeat", self.left)
        base.accept("d" + "-repeat", self.right)
        
        base.accept("e" + "-repeat", self.up)
        base.accept("q" + "-repeat", self.down)
        

    def povortLeft(self):
        self.hero.setH((self.hero.getH() + 5)%360)
    
    def povorotRight(self):
        self.hero.setH((self.hero.getH() - 5)%360)

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def try_move(self, angle):
        pass
    
    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def look_at(self, angle):
        x_start = round(self.hero.getX())
        y_start = round(self.hero.getY())
        z_start = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)

        return x_start + dx, y_start + dy, z_start
    
    def check_dir(self, angle):
        if 20 <= angle < 65:
            return 1, -1
        elif 65 <= angle < 110:
            return 1, 0
        elif 110 <= angle < 155:
            return 1, 1
        elif 155 <= angle < 200:
            return 0, 1
        elif 200 <= angle < 245:
            return -1, 1
        elif 245 <= angle < 290:
            return -1, 0
        elif 290 <= angle < 335:
            return -1, -1
        elif 335 <= angle < 360:
            return 0, -1
        elif 0 <= angle < 20:
            return 0, -1
        
    def forward(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)
    
    def back(self):
        angle = (self.hero.getH()+0) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)

    def up(self):
        z_start = self.hero.getZ()
        self.hero.setZ(z_start+1)
    
    def down(self):
        z_start = self.hero.getZ()
        self.hero.setZ(z_start-1)