class Robot():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.currentDirection = "NORTH"
        self.directions = ["NORTH","EAST","SOUTH","WEST"]
    def turnRight(self):
        i = self.directions.index(self.currentDirection)
        if i == 3:
            self.currentDirection = self.directions[0]
        else:
            self.currentDirection = self.directions[i+1]
    def turnLeft(self):
        i = self.directions.index(self.currentDirection)
        if i == 0:
            self.currentDirection = self.directions[-1]
        else:
            self.currentDirection = self.directions[i-1]
    def forward(self, n):
        if self.currentDirection == "NORTH":
            self.y += n
        elif self.currentDirection == "SOUTH":
            self.y -= n
        elif self.currentDirection == "EAST":
            self.x += n
        elif self.currentDirection == "WEST":
            self.x -= n
