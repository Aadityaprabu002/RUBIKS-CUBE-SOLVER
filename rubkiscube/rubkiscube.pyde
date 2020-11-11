add_library('peasycam')
from Cube import CUBE
from peasy import PeasyCam

import math
dim = 3
cube = []
cam = None
counter = 0
matrix = None
solve = []
resolve = False
def turnX(index,dir):
    global cube,solve,resolve
    if not resolve:
        solve.append(('x',index,-dir))

    for i in range(len(cube)):
        CB = cube[i]
        if CB.posX == index:
            mat = PMatrix2D()
            mat.rotate(dir*HALF_PI)
            mat.translate(CB.posY,CB.posZ)
            CB.turnFaceX(dir)
            CB.update(round(CB.posX),round(mat.m02),round(mat.m12))
            
def turnY(index,dir):
    global cube,solve,resolve
    if not resolve:
        solve.append(('y',index,-dir))
    for i in range(len(cube)):
        CB = cube[i]
        if CB.posY == index:
            mat = PMatrix2D()
            mat.rotate(dir*HALF_PI)
            mat.translate(CB.posX,CB.posZ)
            CB.turnFaceY(dir)
            CB.update(round(mat.m02),round(CB.posY),round(mat.m12))            
            
            
def turnZ(index,dir):
    global cube,solve,resolve
    if not resolve:
        solve.append(('z',index,-dir))
        

    for i in range(len(cube)):
        CB = cube[i]
        if CB.posZ == index:
            mat = PMatrix2D()
            mat.rotate(dir*HALF_PI)
            mat.translate(CB.posX,CB.posY)
            CB.update(round(mat.m02),round(mat.m12),round(CB.posZ))
            CB.turnFaceZ(dir) 
                       
def keyPressed():
    global resolve,counter,solve
    if key == 'f':
        turnZ(-1,1)
    elif key=='F':
        turnZ(-1,-1)
    elif key == 'b': 
        turnZ(-1, 1);
    elif key == 'B': 
        turnZ(-1, -1);
    elif key=='u': 
        turnY(1, 1);
    elif key== 'U': 
        turnY(1, -1);
    elif key== 'd': 
        turnY(-1, 1);
    elif key == 'D': 
        turnY(-1, -1);
    elif key == 'l': 
        turnX(-1, 1);
    elif key == 'L': 
        turnX(-1, -1);
    elif key == 'r': 
        turnX(1, 1);
    elif key == 'R': 
        turnX(1, -1);
    elif key == 'p':
        counter = (len(solve))-1
        resolve = not resolve    

def setup( ):
    global cube,cam
    size(500,500,P3D)
    cam = PeasyCam(this,400)
    leng = 50
    low = -1
    high = 2
    incre = 1
    matrix = PMatrix3D()
    for x in range(CUBE.low,CUBE.high,CUBE.incre):
        for y in range(CUBE.low,CUBE.high,CUBE.incre):
            for z in range(CUBE.low,CUBE.high,CUBE.incre):
                matrix = PMatrix3D()
                matrix.translate(x,y,z)
                cube.append(CUBE(matrix,x,y,z))
                
                
    cube[2].col = color(255,0,0)  
    cube[0].col = color(0,0,255)  
           
def ApplySolution(selector,index,dir):
    if selector == 'x':
            turnX(index,dir)
    elif selector == 'y':
            turnY(index,dir)
    elif selector == 'z':
            turnZ(index,dir) 
                              
def draw():
    global pathLen,counter,solve,resolve
    
    background(255)
    scale(50)
    global cube
    for i in range(len(cube)):
            cube[i].show()
            
    if resolve:
        if counter>=0:
            ApplySolution(solve[counter][0],
                          solve[counter][1],
                          solve[counter][2])
            counter-=1
        else:
            resolve = False
            solve = []
            counter = 0
        
        
                
            
