# Maze-Generation (Procedural Content Generation)
A random maze generation using procedural content generation techniques for the gaming world

### Prefab elements: 

To develop the maze, we have divided the canvas into the cells of a specific grid size. In the image below the cell size is 20. In the beginning the cells are shown with all the 4 borders of green color and as the algorithm starts creating the maze, it removes the walls between cells and change the color of the cell to purple. The highlighted cell is the current cell in which the algorithm is exploring to create the maze in the grid. 

Once the algorithm is done creating the maze, the final maze will look like the Image 3 where the path is shown in purple and walls are in light green. 

![alt text](https://github.com/ayushjain94/Maze-Generation/blob/master/images/Maze.png?raw=true)


## Depth First Backtracking: 

The algorithm used to create the maze is Depth First Backtracking. Initially the grid is divided into the cells of a specific size in such a way so that the whole canvas of 640 X 480 can be completely split into the cells. We choose the grid size which can divide the 640 and 480 both because this will generate the number of cells which can be accommodate in this canvas without any overflow. This is shown in the Image 1 above. Each cell has four walls. 

The algorithm is implemented using Stack which follows last in first out order for the nodes to be explored. In the beginning, the algorithm chooses a random cell and check all four neighbors and choose one randomly to expand which has not already been visited. Once the neighbor is chosen, the algorithm marks it as visited so that it doesn’t get explored while looking up for the neighbors later and it removes the wall between the two cells based on chosen neighbor. The neighbor is then added to the stack for the backtracking. This process keep continues till it finds a cell with no unvisited neighbors and then it starts backtracking by popping cells from the stack and again repeat the same procedure. This process continues till all the cells has been visited and also complete the backtracking all the way back to the initial cell from where the algorithm started. 

Algorithm maintains an array of 4 Booleans for each cell which is set to False when that particular wall is needed to be removed. To connect one cell from another, two walls need to be removed one for the cell1 and another overlapping wall of the cell2. 

We have used the iteration version of the DFS backtracking as it’s easier to display the maze formation in the processing, we can change it to recursive implementation easily. The algorithm doesn’t take much time to generate the maze it’s very fast since I am simulating the formation in the code so it can take time. We can increase this by setting the frame rate to higher. Also, we can generate the maze in setup instead of draw that will take few seconds to generate the maze even with small grid size but then we won’t be able to simulate the formation. 

We also keep track of the previous node in the algorithm as it allows us to stop highlighting the last cell once the maze is generated. We compare the previous node with the current node if these are not equal then keep highlighting otherwise don’t highlight. 


The maze generation can be tweaked by changing certain parameters: 

1. Grid Size: This can be changed in the assignment3_file on line number 7. By default the value is 20. It can be changed to any number which can divded the height and width both of th canvas. 

E.g.: 10, 20, 40

2. Neighbours: Neighbors can be chosen randomly or in an order. There are few lines in file Maze.py from 45 to 47. By default the behaviour is random but it can be changed by uncommneting the other behaviour and commmenting random on these lines. 

3. Beginning Cell: The generation can start from any cell of the game, this can be tweaked from lines 25 to 29 of assignment_3 file. Default behaviour is random whereas it can be changed by commenting/uncommenting these lines. 

The algorithm and implementation is not slow, just to show the formation, i have kept the DFS in the draw method incase we don't wish to see generation then we can do this computation in setup and that would generate the maze in few seconds. 