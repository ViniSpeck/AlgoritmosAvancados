from command.command import *
import settings
from solver import solve_maze

start_symbol = 'S'

cache = dict()

def get_path(file_path):
    maze = read_file(file_path)
    start = find_variables(start_symbol,maze)
    path=(start,)
    maze_hash = hash(draw_maze(maze, path))
    if maze_hash not in cache:
        solve_maze(maze,path)
        cache[maze_hash] = settings.path_drawing
    else:
        print(cache[maze_hash])
        return 0