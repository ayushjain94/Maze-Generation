class GridCell:
    def __init__(self, id, grid_size, x, y):
        self.id = id
        self.size = grid_size
        self.position = PVector(y * self.size, x * self.size)
        self.divider = [True] * 4
        self.visited = False
        self.pathVisited = False
        self.x = x
        self.y = y
    
    
    def display(self):
        stroke(136, 202, 87)
        if (self.divider[0]):
            line(self.position.x, self.position.y, self.position.x+self.size, self.position.y);
        if (self.divider[1]):
            line(self.position.x + self.size, self.position.y, self.position.x+self.size, self.position.y+self.size);
        if (self.divider[2]):
            line(self.position.x + self.size, self.position.y + self.size, self.position.x, self.position.y + self.size);
        if (self.divider[3]):
            line(self.position.x, self.position.y + self.size, self.position.x, self.position.y);
        noStroke()
        fill(101, 31, 255, 100)
        if(self.visited):
            rect(self.position.x, self.position.y, self.size, self.size)

    def highlight(self):
        fill(233, 30, 99)
        rect(self.position.x,self.position.y,self.size,self.size);
        
