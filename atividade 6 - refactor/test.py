import unittest
from command.maze import Maze

maze_list = ['mazes/001.txt','mazes/002.txt','mazes/003.txt','mazes/004.txt']#,'mazes/005.txt','mazes/006.txt','mazes/007.csv']

class TestMaze(unittest.TestCase):
    def test_maze_structure(self):
        allowed_characters = ('#','.','S','E','C')
        for maze in maze_list:
            maze = Maze.read_file(maze)
            for row in maze:
                for square in row:
                    self.assertTrue(square in allowed_characters)

    def test_maze_variables(self):
        for maze in maze_list:
            maze = Maze.read_file(maze)
            if Maze.count_variable('S',maze)==1 and Maze.count_variable('E',maze)>=1:
                continue
            else:
                self.assertEqual(0, 1)
        self.assertEqual(1, 1)

    def test_file_type(self):
        for maze in maze_list:
            self.assertEqual(maze[-4:], '.txt')
        pass

if __name__ == '__main__':
    unittest.main()