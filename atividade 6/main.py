from command.command import *
from command.get_path import get_path
import settings

maze_list = ['mazes/001.txt','mazes/002.txt','mazes/003.txt','mazes/004.txt']

if __name__ == "__main__":
    while True:
        settings.init()
        choice = input(f"Choose a maze (1 to {len(maze_list)}, ENTER to leave): ")
        if choice != '' and 'c':
            get_path(maze_list[int(choice)-1])
        else:
            break
