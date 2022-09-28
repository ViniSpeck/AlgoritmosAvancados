def find_variables(character, maze):
        for i, j in enumerate(maze):
            try:
                return (i, j.index(character))
            except ValueError:
                pass