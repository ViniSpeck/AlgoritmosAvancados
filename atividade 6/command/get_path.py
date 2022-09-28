from command.command import *

def get_path(maze, cache):
    if hash(maze) not in cache:
        cache[hash(maze)] = create_path()