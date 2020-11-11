from Face import FACE
class CUBE:
    leng =1
    low = -leng
    high = leng+1
    incre = leng
    def __init__(self,mat,x,y,z):
        self.posX = x
        self.posY = y
        self.posZ = z
        self.matrix = mat
        self.col = color(255)
        self.faces = [0]*6
        self.faces[0] = FACE(PVector(0,0,-1),color(0,0,255))
        self.faces[1] = FACE(PVector(0,0,1),color(0,255,0))     
        self.faces[2] = FACE(PVector(0,1,0),color(255,255,255))
        self.faces[3] = FACE(PVector(0,-1,0),color(255,255,0))
        self.faces[4] = FACE(PVector(1,0,0),color(255,150,0))
        self.faces[5] = FACE(PVector(-1,0,0),color(255,0,0))
    
        
    def show(self):
        
        noFill()
        stroke(0)
        strokeWeight(0.05)
        pushMatrix()
        applyMatrix(self.matrix)
        box(CUBE.leng)
        for face in self.faces:
            face.fillcolor()
        popMatrix()
        
    def update(self,changeX,changeY,changeZ): 
         self.matrix.reset()
         self.matrix.translate(changeX,changeY,changeZ)
         self.posX = changeX
         self.posY = changeY
         self.posZ = changeZ
         
    def turnFaceZ(self,dir): 
       for face in self.faces:
           face.turnZ(dir*HALF_PI)
    def turnFaceX(self,dir): 
       for face in self.faces:
           face.turnX(dir*HALF_PI)
    def turnFaceY(self,dir):
       for face in self.faces:
           face.turnY(dir*HALF_PI)         
         
        
        
             
        
