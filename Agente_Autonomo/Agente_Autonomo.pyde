from Vehicle import Vehicle
from Food import Food

position = PVector(0, 0)

def setup():
    global v
    global f
    global position
    size(640, 360)
    
    v = Vehicle(width / 2, height / 2)
    
    position = PVector(random(0, 640), random(0, 360))
    f = Food(position.x, position.y)

def draw():
    global position
    global f
    
    background(51)
    
    v.arrive(position)
    
    f.update()
    f.display()
    
    v.update()
    v.display()
    
    if (v.isColliding(position)):
        position = PVector(random(0, 640), random(0, 360))
        f = Food(position.x, position.y)
        v.scored()
