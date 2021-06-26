from Vehicle import Vehicle
from Food import Food
from Map import Map
from Pathfinding import Pathfinding

search = None
waiting = 0
found = False
keysPosition = 640

def setup():
    size(800, 640)
    
    reset()
    
def draw():
    global position
    global v
    global f
    global path
    global waiting
    global found
    global search
    global keysPosition
    
    if (search == None):
        m.display()
        f.display()
        v.display()
        
        if (keysPosition > 529):
            keysPosition -= 15
        
        image(photo, 191, keysPosition)
    elif (keysPosition < 640):
        keysPosition += 15
        m.display()
        f.display()
        v.display()
        
        image(photo, 191, keysPosition)
    elif (found == False):
        found = path.update()
    elif (waiting < 100):
        waiting += 1
    else:
        background(255, 119, 81)
        
        v.arrive(position, m.get_speed(PVector(position.x / m.gridSize, position.y / m.gridSize)))
        
        m.display()
        
        f.update()
        f.display()
        
        v.update()
        v.display()
        
        if (v.isColliding(f.position)):
            v.scored()
            
            positionFood = m.random_position()
            f = Food(positionFood.x * m.gridSize + m.gridSize / 2, positionFood.y * m.gridSize + m.gridSize / 2)
            
            m.display()
            
            f.update()
            f.display()
            
            v.update()
            v.display()
            
            waiting = 0
            search = None
            found = False
        elif (v.isColliding(position)):
            position = path.path.pop()
            
def reset():
    global v
    global f
    global m
    global position
    global photo
    global search
    global waiting
    global found
    global keysPosition
    
    search = None
    waiting = 0
    found = False
    keysPosition = 640
    
    photo = loadImage("keys.png")

    m = Map(16)
    
    positionVehicle = m.random_position()
    positionFood = m.random_position()
    
    v = Vehicle(positionVehicle.x * m.gridSize + m.gridSize / 2, positionVehicle.y * m.gridSize + m.gridSize / 2)
    f = Food(positionFood.x * m.gridSize + m.gridSize / 2, positionFood.y * m.gridSize + m.gridSize / 2)
    
    m.display()
    
    f.update()
    f.display()
    
    v.update()
    v.display()

    position = v.position
            
def keyPressed():
    global search
    global path
    
    if key == 'r' or key == 'R':
        reset()
            
    if (search == None and keysPosition <= 529):
        if key == 'a' or key == 'A':
            path = Pathfinding(m, v, f, 'a')
            search = 'a'
        
        if key == 'l' or key == 'L':
            path = Pathfinding(m, v, f, 'l')
            search = 'l'
            
        if key == 'c' or key == 'C':
            path = Pathfinding(m, v, f, 'c')
            search = 'c'

        if key == 'g' or key == 'G':
            path = Pathfinding(m, v, f, 'g')
            search = 'g'
            
        if key == 'p' or key == 'P':
            path = Pathfinding(m, v, f, 'p')
            search = 'p'
