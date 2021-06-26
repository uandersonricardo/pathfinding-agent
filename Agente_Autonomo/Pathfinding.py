from Structures import Queue, Stack, PriorityQueue

class Pathfinding():
    def __init__(self, m, v, f, s):
        self.m = m
        self.v = v
        self.f = f
        self.s = s
        
        if s == 'l':
            self.frontier = Queue()
        elif s == 'p':
            self.frontier = Stack()
        else:
            self.frontier = PriorityQueue()
            
        self.path = []
        
        position = self.position_grid(v.position)
        
        self.frontier.put(position, 0)
        self.came_from = dict()
        self.cost_so_far = dict()
        self.came_from[str(position)] = None
        self.cost_so_far[str(position)] = 0


    def update(self):
        if not self.frontier.empty():
            current = self.frontier.get()
            
            noStroke()
            
            fill(0, 38, 219, 60)
        
            rect(current.x * self.m.gridSize, current.y * self.m.gridSize, self.m.gridSize, self.m.gridSize)
            
            if current.x == int(self.f.position.x / self.m.gridSize) and current.y == int(self.f.position.y / self.m.gridSize): 
                self.printPath(current)
                return True
            
            for next in self.neighbors(current):
                new_cost = None
                
                if (self.s == 'a' or self.s == 'c'):
                    new_cost = self.cost_so_far[str(current)] + self.m.get_cost(next)
                else:
                    new_cost = 1
    
                if str(next) not in self.cost_so_far or new_cost < self.cost_so_far[str(next)]:
                    self.cost_so_far[str(next)] = new_cost
                    
                    priority = None
                    if (self.s == 'a'):
                         priority = new_cost + self.heuristic(next)
                    elif (self.s == 'g'):
                         priority = self.heuristic(next)
                    else:
                         priority = new_cost
                         
                    self.frontier.put(next, priority)
                    self.came_from[str(next)] = current
        
        return False
    
    def heuristic(self, a):
        b = PVector(int(self.f.position.x / self.m.gridSize), int(self.f.position.y / self.m.gridSize))
        return abs(a.x - b.x) + abs(a.y - b.y)
    
    def position_grid(self, position):
        return PVector(int(position.x / self.m.gridSize), int(position.y / self.m.gridSize))
    
    def neighbors(self, position):
        res = []
        
        if (position.x > 0 and self.m.grid[int(position.x - 1)][int(position.y)] != 3):
            res.append(PVector(position.x - 1, position.y))
            
        if (position.y > 0 and self.m.grid[int(position.x)][int(position.y - 1)] != 3):
            res.append(PVector(position.x, position.y - 1))
            
        if (position.x < (width / self.m.gridSize) - 1 and self.m.grid[int(position.x + 1)][int(position.y)] != 3):
            res.append(PVector(position.x + 1, position.y))
            
        if (position.y < (height / self.m.gridSize) - 1 and self.m.grid[int(position.x)][int(position.y + 1)] != 3):
            res.append(PVector(position.x, position.y + 1))
        
        return res
    
    def printPath(self, current):
        noStroke()
        fill(239, 15, 2, 60)
        
        came = current
        
        while came != None:
            self.path.append(PVector(came.x * self.m.gridSize + self.m.gridSize / 2, came.y * self.m.gridSize  + self.m.gridSize / 2))
            rect(came.x * self.m.gridSize, came.y * self.m.gridSize, self.m.gridSize, self.m.gridSize)
            came = self.came_from[str(came)]
