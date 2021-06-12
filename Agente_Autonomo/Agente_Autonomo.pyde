from Vehicle import Vehicle
from Food import Food

def setup():
    global v
    global f
    size(640, 360)
    v = Vehicle(width / 2, height / 2)
    f = Food(600, height / 2)

def draw():
    background(51)

    mouse = PVector(mouseX, mouseY)

    v.arrive(mouse)
    
    f.update()
    f.display()
    
    v.update()
    v.display()
    
    print(v.isColliding(PVector(600 + 3, height / 2 + 3)))
