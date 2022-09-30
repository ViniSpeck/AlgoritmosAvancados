import settings
import os, time

class Solver:
	def __str__(maze, path):
		os.system('cls')
		
		for square in path:
			maze[square[0]][square[1]] = "-"
		maze[path[-1][0]][path[-1][1]] = "~"

		maze_drawing = ""
		
		for row in maze:
			for square in row:
				square = str(square).replace("#","▓")
				square = str(square).replace("."," ")
				square = str(square).replace("X"," ")
				maze_drawing += square
			maze_drawing += "\n"
		return maze_drawing

	def solve_maze(maze,path):
			mouse = path[-1]
			print(Solver.__str__(maze,path))
			possible_moves = [(mouse[0]+1,mouse[1]),(mouse[0]-1,mouse[1]),(mouse[0],mouse[1]+1),(mouse[0],mouse[1]-1)]

			for move in possible_moves:
				time.sleep(0.02)
				if maze[move[0]][move[1]] == 'E':
					path += (move,)
					settings.path_drawing=Solver.__str__(maze,path)
					print(settings.path_drawing)
					input("Rato livre")
					os.system('cls')
				elif maze[move[0]][move[1]] in ['#','X']:
					continue
				elif move in path:
					continue
				else:
					correct_path = path + (move,)
					Solver.solve_maze(maze,correct_path)
					maze[move[0]][move[1]]='X'
					print(Solver.__str__(maze,path))