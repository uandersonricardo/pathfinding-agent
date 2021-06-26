class Food():
    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, 0)
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 1.0
        self.maxforce = 0.01
        self.opacity = 255
        self.bg = 0

    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        self.acceleration.mult(0)

    def applyForce(self, force):
        self.acceleration.add(force)

    def display(self):
        theta = self.velocity.heading()
        
        if self.opacity <= 80:
            self.opacity = 255
            self.bg = (self.bg + 1) % 5
        else:
            self.opacity = self.opacity - 12
        
        if (self.bg == 0):
            fill(255, 0, 255, self.opacity)
        elif (self.bg == 1):
            fill(255, 255, 0, self.opacity)
        elif (self.bg == 2):
            fill(255, 0, 0, self.opacity)
        elif (self.bg == 3):
            fill(0, 255, 0, self.opacity)
        elif (self.bg == 4):
            fill(0, 0, 255, self.opacity)
            
        noStroke()
        with pushMatrix():
            translate(self.position.x - self.r / 2, self.position.y - self.r / 2)
            rotate(theta)
            rect(0, 0, self.r, self.r)
