import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_maze_create_cells_again(self):
        num_cols = 0
        num_rows = 0
        with self.assertRaises(ValueError):
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        first_cell = m1._cells[0][0]
        last_cell = m1._cells[-1][-1]
        self.assertFalse(first_cell.has_left_wall)
        self.assertFalse(last_cell.has_right_wall)

if __name__ == "__main__":
    unittest.main()
