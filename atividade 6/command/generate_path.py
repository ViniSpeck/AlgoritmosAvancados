from command.command import *

def generate_path(file_path,start_symbol):
    maze = file_reader(file_path)
    start = find_variables(start_symbol,maze)
    path=(start,)
    maze_solver(maze,path)