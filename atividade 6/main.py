from command.command import *
from solver import maze_solver

file_path = 'fixtures/004.txt'
start_symbol = 'S'

if __name__ == "__main__":
    maze = file_reader(file_path)
    start = find_variables(start_symbol,maze)
    path=(start,)
    maze_solver(maze,path)