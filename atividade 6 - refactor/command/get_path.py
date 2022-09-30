from command.maze import Maze
from command.solver import Solver
import settings

class GetPath:
    start_symbol = 'S'
    cache = dict()

    def __init__(self, start_symbol, cache):
        self.start_symbol = start_symbol
        self.cache = cache
    
    def get_path(file_path):
        maze = Maze.read_file(file_path)
        start = Maze.find_variables(GetPath.start_symbol,maze)
        path=(start,)
        maze_hash = hash(Solver.__str__(maze,path))
        if maze_hash not in GetPath.cache:
            Solver.solve_maze(maze,path)
            GetPath.cache[maze_hash] = settings.path_drawing
        else:
            print(GetPath.cache[maze_hash])
            return 0