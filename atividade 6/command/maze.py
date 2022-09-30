class Maze:
    def __init__(self,path):
        self.path = path
    
    def read_file(path):
        maze = []
        file = open(path)
        for line in file.read().splitlines():
            maze.append(list(line))
        file.close()
        return maze
    
    def find_variables(character, maze):
        for i, j in enumerate(maze):
            try:
                return (i, j.index(character))
            except ValueError:
                pass

    def count_variable(character,maze):
        variable = 0
        for row in maze:
                for square in row:
                    if square == character:
                        variable+=1
                    else:
                        pass
        return variable