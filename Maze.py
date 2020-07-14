import random
class Maze:
    def __init__(self, rows, columns):
        self.cells = {}
        self.rows = rows
        self.columns = columns
    
    
    def remove_dividers(self, cell1, cell2):
        diff_x = cell1.x - cell2.x
        if (diff_x == 1):
            cell1.divider[0] = False
            cell2.divider[2] = False
        elif (diff_x == -1):
            cell1.divider[2] = False
            cell2.divider[0] = False
        
        diff_y = cell1.y - cell2.y
        if(diff_y == 1):
            cell1.divider[3] = False
            cell2.divider[1] = False
        
        elif(diff_y == -1):
            cell1.divider[1] = False
            cell2.divider[3] = False
                                
                                                    
    def valid_cell(self, x, y):
        if (0 <= x < self.rows) and (0 <= y < self.columns):
            return True
        else:
            return False    

    def look_up_neighbours(self, grid_cell):
        id = grid_cell.id
        #Top Cell
        x,y= grid_cell.x, grid_cell.y
        possible_neighbours = [(x,y-1,id-1), (x+1,y,id+self.columns), (x-1,y,id-self.columns), (x,y+1,id+1)] #left , bottom, top, right
        neighbours = []
        for i,j,new_id in possible_neighbours:
            if self.valid_cell(i,j):
                if not self.cells[new_id].visited:
                    neighbours.append(new_id)
        if len(neighbours) > 0:
            return self.cells[random.choice(neighbours)]
            # return self.cells[neighbours[0]] #Follows this order #left , bottom, top, right
            # return self.cells[neighbours[-1]] #Follows this order #right, top, bottom, left
        else:
            return None
