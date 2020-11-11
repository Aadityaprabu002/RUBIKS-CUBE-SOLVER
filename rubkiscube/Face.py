class FACE:
    
    def __init__(self,normal,col):
        self.normal = normal
        self.col = col
        
    def fillcolor(self):
        pushMatrix()
        noStroke()
        fill(self.col)
        rectMode(CENTER)
        
        translate(self.normal.x * 0.5,
                  self.normal.y * 0.5,
                  self.normal.z * 0.5)
        
        if abs(self.normal.z) >0:
            rotateZ(HALF_PI)
        elif abs(self.normal.x) >0:
            rotateY(HALF_PI)
        elif abs(self.normal.y)>0:
            rotateX(HALF_PI)  

        square(0,0,1)
        popMatrix()
    def turnZ(self,angle):
        V = PVector()
        n = self.normal
        V.x = round(n.x*cos(angle) - n.y*sin(angle))
        V.y = round(n.x*sin(angle) + n.y*cos(angle))
        V.z = round(n.z)
        self.normal = V
          
    def turnY(self,angle):
        V = PVector()
        n = self.normal
        V.x = round( n.x*cos(angle) - n.z*sin(angle))
        V.y = round(n.y)
        V.z = round(n.x*sin(angle) + n.z*cos(angle))
        self.normal = V
        
    def turnX(self,angle):  
        V = PVector()
        n = self.normal
        V.x = round(n.x)
        V.y = round(n.y*cos(angle) - n.z*sin(angle))
        V.z = round(n.y*sin(angle) + n.z*cos(angle))
        self.normal = V            
            
        
        
