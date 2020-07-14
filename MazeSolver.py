class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.path = None
        
    def get_neighbours(self, cell):
        x = cell.x
        y = cell.y
        id = cell.id
        neighbours = []
        probable_neighbours = [(x-1,y,id-self.maze.columns), (x,y+1,id+1), (x+1,y,id+self.maze.columns), (x,y-1,id-1)]
        
        for i in range(4):
            if not cell.divider[i]:
                i,j,new_id = probable_neighbours[i]
                if (0 <= i < self.maze.rows) and (0 <= j < self.maze.columns) and not self.maze.cells[new_id].pathVisited:
                    neighbours.append(new_id)
        return neighbours 
   
    def print_path(self):
        stroke(0)
        strokeWeight(10);
        for cell in self.path:
            line(cell.position.x, cell.position.y / 2, cell.position.x+cell.size, cell.position.y / 2);
        noStroke()
        strokeWeight(1);
        
        
    def solve(self):
        stack = [self.maze.cells[0]]
        goal_node_id = (self.maze.columns * self.maze.rows) - 1
        path = []
        expanded_node = None
        path.append(self.maze.cells[0])
        while expanded_node is not None or len(stack) > 0:
            current_node = stack.pop()
            path.pop()
            neighbours = self.get_neighbours(current_node)
            if goal_node_id in neighbours:
                print('Path Found')
                self.path = path
                return True
            while len(neighbours) > 0:
                expanded_node = self.maze.cells[neighbours[0]]
                expanded_node.pathVisited = True
                stack.append(current_node)
                path.append(current_node)
                current_node = expanded_node
                neighbours = self.get_neighbours(current_node)
                if goal_node_id in neighbours:
                    print('Path Found')
                    self.path = path
                    return

    
        
        
        
       
        
