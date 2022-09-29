def read_file(path):
    maze = []
    file = open(path)
    for line in file.read().splitlines():
        maze.append(list(line))
    return maze