class Vehicle():
    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, -2)
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 4
        self.maxforce = 0.2
        self.score = 0

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)
        
    def scored(self):
        self.score += 1

    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def arrive(self, target):

        # A vector pointing from the location to the target
        desired = target - self.position
        d = desired.mag()

        # Scale with arbitrary damping within 100 pixels
        if (d < 100):
            m = map(d, 0, 100, 0, self.maxspeed)
            desired.setMag(m)
        else:
            desired.setMag(self.maxspeed)

        # Steering = Desired minus velocity
        steer = desired - self.velocity
        steer.limit(self.maxforce)  # Limit to maximum steering force

        self.applyForce(steer)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading() + PI / 2
        fill(127)
        stroke(200)
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            beginShape()
            vertex(0, -self.r * 2)
            vertex(-self.r, self.r * 2)
            vertex(self.r, self.r * 2)
            endShape(CLOSE)
            
        fill(255)
        textSize(14)
        text(str(self.score), self.position.x + self.r * 2 + 3, self.position.y + self.r * 2 + 4)
        
    def isColliding(self, P):
        theta = self.velocity.heading() + PI / 2
        A = PVector(0, -self.r * 2)
        B = PVector(-self.r, self.r * 2)
        C = PVector(self.r, self.r * 2)
        A.rotate(theta)
        A.add(self.position)
        B.rotate(theta)
        B.add(self.position)
        C.rotate(theta)
        C.add(self.position)
           
        v0 = PVector.sub(C, A)
        v1 = PVector.sub(B, A)
        v2 = PVector.sub(P, A)

        dot00 = PVector.dot(v0, v0)
        dot01 = PVector.dot(v0, v1)
        dot02 = PVector.dot(v0, v2)
        dot11 = PVector.dot(v1, v1)
        dot12 = PVector.dot(v1, v2)
    
        invDenom = 1 / (dot00 * dot11 - dot01 * dot01)
        u = (dot11 * dot02 - dot01 * dot12) * invDenom
        v = (dot00 * dot12 - dot01 * dot02) * invDenom
    
        return (u >= 0) and (v >= 0) and (u + v < 1)
        
