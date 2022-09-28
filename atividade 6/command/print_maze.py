import os

def print_maze(maze, path):
    temp_maze=maze[:]
    os.system('cls')
    
    for square in path:
        temp_maze[square[0]][square[1]] = "-"
    temp_maze[path[-1][0]][path[-1][1]] = "~"

    maze_drawing = ""
    
    for row in temp_maze:
        for square in row:
            square = str(square).replace("#","▓")
            square = str(square).replace("."," ")
            square = str(square).replace("X"," ")
            maze_drawing += square
        maze_drawing += "\n"
    print(maze_drawing)