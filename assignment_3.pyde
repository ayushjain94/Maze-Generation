import json
import random
from GridCell import GridCell
from Maze import Maze
from MazeSolver import MazeSolver

maze, total_grid_cells,grid_size, stack, current_node, previous_node,path_found, solver,playerImg = None, None, 40, [], None, None,False, None, None


def setup():
    global maze, total_grid_cells, GridCell, current_node,playerImg
    size(640, 480)
    frameRate(500)
    rows = height/grid_size;
    columns = width/grid_size;
    grid_id = 0
    maze = Maze(rows, columns)
    for x in range(rows):
        for y in range(columns):
            cell = GridCell(grid_id, grid_size, x, y)
            maze.cells[grid_id] = cell
            grid_id += 1
    
    total_grid_cells = len(maze.cells)
    #stack.append(maze.cells[0]) #Start from the first cell
    # stack.append(maze.cells[(columns * rows) - 1]) #Start from the last cell
    # stack.append(maze.cells[((columns * rows) / 2 )+ columns / 2]) #Start from the middle or center
    # stack.append(maze.cells[columns-1]) #Start Top right cell
    # stack.append(maze.cells[columns * (rows-1)]) #Start Bottom left cell
    randomelement = random.choice(maze.cells)
    stack.append(randomelement)
    current_node = stack.pop()
    
def draw():
    global current_node,previous_node, path_found, solver, grid_size
    background(11, 25, 36);
    for i in range(total_grid_cells):
        maze.cells[i].display()
        
    previous_node = current_node
    expanded_node = maze.look_up_neighbours(current_node)
    if expanded_node is not None:
        expanded_node.visited = True
        stack.append(current_node)
        maze.remove_dividers(current_node, expanded_node)
        current_node = expanded_node
    elif len(stack) > 0:
        current_node = stack.pop()
    if previous_node != current_node:
        current_node.highlight()
    


        
        
        
        
        
    
        
    
    
