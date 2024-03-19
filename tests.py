import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_break_entry_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertFalse(m1.cells[0][0].top)
        self.assertFalse(m1.cells[11][9].bottom)

    def test_maze_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)

        m1._reset_cells_visited()
        for i in range(num_rows):
            self.assertEqual(
                list(map(lambda c: c.visited, m1.cells[i])),
                [False] * num_cols
            )

if __name__ == "__main__":
    unittest.main()

