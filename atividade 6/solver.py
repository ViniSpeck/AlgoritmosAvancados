from command.command import *
from command.draw_maze import draw_maze
import settings
import sys, os, time

def solve_maze(maze,path):
		mouse = path[-1]
		print(draw_maze(maze,path))
		possible_moves = [(mouse[0]+1,mouse[1]),(mouse[0]-1,mouse[1]),(mouse[0],mouse[1]+1),(mouse[0],mouse[1]-1)]

		for move in possible_moves:
			time.sleep(0.02)
			if maze[move[0]][move[1]] == 'E':
				path += (move,)
				settings.path_drawing=draw_maze(maze,path)
				print(settings.path_drawing)
				input("Rato livre")
				os.system('cls')
			elif maze[move[0]][move[1]] in ['#','X']:
				continue
			elif move in path:
				continue
			else:
				correct_path = path + (move,)
				solve_maze(maze,correct_path)
				maze[move[0]][move[1]]='X'
				print(draw_maze(maze,path))