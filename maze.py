import random
import time
from cell import Cell
from graphics import Window
from typing import Optional


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Optional[Window],
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.delay = 0.01
        self.cells = []
        for _ in range(self.num_cols):
            self.cells.append([None] * num_rows)

        self._create_cells()
        self._break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self.delay = 0.05
        self.solve()

    def _create_cells(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.cells[i][j] = Cell(self.win)
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        entry = self.cells[0][0]
        entry.top = False
        self._draw_cell(0, 0)
        goal = self.cells[self.num_cols - 1][self.num_rows - 1]
        goal.bottom = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _draw_cell(self, i, j):
        x = self.x1 + i * self.cell_size_x
        y = self.y1 + j * self.cell_size_y

        self.cells[i][j].draw(x, y, x + self.cell_size_x, y + self.cell_size_y)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(self.delay)

    def _break_walls_r(self, i, j):
        current_cell = self.cells[i][j]
        current_cell.visited = True
        directions = {
                'left': (-1, 0),
                'right': (1, 0),
                'up': (0, -1),
                'down': (0, 1),
        }
        while True:
            to_visit = []
            for dir in directions.keys():
                x = i + directions[dir][0]
                y = j + directions[dir][1]
                if x >= 0 and x < self.num_cols and y >= 0 and y < self.num_rows:
                    if not self.cells[x][y].visited:
                        to_visit.append(dir)

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            dir = random.choice(to_visit)
            x = i + directions[dir][0]
            y = j + directions[dir][1]

            next_cell = self.cells[x][y]
            if dir == 'left':
                current_cell.left = False
                next_cell.right = False
            if dir == 'right':
                current_cell.right = False
                next_cell.left = False
            if dir == 'up':
                current_cell.top = False
                next_cell.bottom = False
            if dir == 'down':
                current_cell.bottom = False
                next_cell.top = False

            self._break_walls_r(x, y)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self.cells[i][j]
        current_cell.visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        if not current_cell.right:
            other_cell = self.cells[i + 1][j]
            if not other_cell.visited:
                current_cell.draw_move(other_cell)
                if self._solve_r(i + 1 ,j):
                    return True
                current_cell.draw_move(other_cell, True)
        if not current_cell.left:
            other_cell = self.cells[i - 1][j]
            if not other_cell.visited:
                current_cell.draw_move(other_cell)
                if self._solve_r(i - 1 ,j):
                    return True
                current_cell.draw_move(other_cell, True)
        if not current_cell.top and i != 0 and j != 0:
            other_cell = self.cells[i][j - 1]
            if not other_cell.visited:
                current_cell.draw_move(other_cell)
                if self._solve_r(i, j - 1):
                    return True
                current_cell.draw_move(other_cell, True)
        if not current_cell.bottom:
            other_cell = self.cells[i][j + 1]
            if not other_cell.visited:
                current_cell.draw_move(other_cell)
                if self._solve_r(i, j + 1):
                    return True
                current_cell.draw_move(other_cell, True)
        return False



