from command.command import *
from command.print_maze import print_maze
import sys, os, time

def maze_solver(maze,path):
	mouse = path[-1]
	print_maze(maze,path)
	possible_moves = [(mouse[0]+1,mouse[1]),(mouse[0]-1,mouse[1]),(mouse[0],mouse[1]+1),(mouse[0],mouse[1]-1)]

	for move in possible_moves:
		time.sleep(0.02)
		if maze[move[0]][move[1]] == 'E':
			path += (move,)
			print_maze(maze,path)
			input("Rato livre")
			os.system('cls')
			sys.exit()
		elif maze[move[0]][move[1]] in ['#','X']:
			pass
		elif move in path:
			pass
		else:
			correct_path = path + (move,)
			maze_solver(maze, correct_path)
			maze[move[0]][move[1]]='X'
			print_maze(maze,path)
