class Map():
    def __init__(self, gridSize):
        self.gridSize = gridSize
        self.noiseScale = random(7, 10)
        self.offsetX = random(1, 100)
        self.offsetY = random(1, 100)
        self.gridWidth = width / gridSize
        self.gridHeight = height / gridSize
        self.grid = []
        
        for y in range(self.gridHeight):
            for x in range(self.gridWidth):
                if (y == 0):
                    self.grid.append([])
                    
                nx = float(x) / self.gridWidth - 0.5
                ny = float(y) / self.gridHeight - 0.5
                
                noiseVal = noise(nx * self.noiseScale + self.offsetX, ny * self.noiseScale + self.offsetY)
                
                if (noiseVal <= 0.4):
                    self.grid[x].append(0)
                elif (noiseVal <= 0.45):
                    self.grid[x].append(3)
                elif (noiseVal <= 0.65):
                    self.grid[x].append(1)
                elif (noiseVal <= 0.7):
                    self.grid[x].append(3)
                else:
                    self.grid[x].append(2)

    def display(self):
        for y in range(self.gridHeight):
            for x in range(self.gridWidth):
                noStroke()
                
                if (self.grid[x][y] == 0):
                    fill(230, 230, 179)
                elif (self.grid[x][y] == 1):
                    fill(167, 152, 118)
                elif (self.grid[x][y] == 2):
                    fill(140, 191, 217)
                else:
                    fill(90, 90, 90)
            
                rect(x * self.gridSize, y * self.gridSize, self.gridSize, self.gridSize)
    
    def random_position(self):
        position = None
        while(True):
            position = PVector(int(random(0, self.gridWidth)), int(random(0, self.gridHeight)))
            
            if (self.grid[int(position.x)][int(position.y)] != 3):
                return position
            
    def get_cost(self, position):
        terrain = self.grid[int(position.x)][int(position.y)]
        
        if (terrain == 0):
            return 1

        if (terrain == 1):
            return 5
        
        if (terrain == 2):
            return 10
        
        return 999999
    
    def get_speed(self, position):
        terrain = self.grid[int(position.x)][int(position.y)]
        
        if (terrain == 0):
            return 10

        if (terrain == 1):
            return 5
        
        if (terrain == 2):
            return 1
        
        return 0
