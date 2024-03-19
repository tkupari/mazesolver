from graphics import Window, Point, Line
from typing import Optional


class Cell:
    def __init__(self, window: Optional[Window]) -> None:
        self.left = True
        self.right = True
        self.top = True
        self.bottom = True
        self.window = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.top_left = Point(x1, y1)
        self.top_right = Point(x2, y1)
        self.bottom_left = Point(x1, y2)
        self.bottom_right = Point(x2, y2)

        self._draw_line(self.top_left, self.bottom_left, self.left)
        self._draw_line(self.top_right, self.bottom_right, self.right)
        self._draw_line(self.top_left, self.top_right, self.top)
        self._draw_line(self.bottom_left, self.bottom_right, self.bottom)


    def _draw_line(self, start, finish, enabled):
        if self.window is None:
            return
        l = Line(start, finish)
        color = "black"
        if not enabled:
            color = "white"
        self.window.draw_line(l, color)

    def draw_move(self, to_cell, undo=False):
        if self.window is None:
            return
        l = Line(self.center, to_cell.center)
        color = "red"
        if undo:
            color = "grey"
        self.window.draw_line(l, color)

    @property
    def center(self):
        return Point(
                (self.top_left.x + self.top_right.x) / 2,
                (self.top_left.y + self.bottom_left.y) / 2
        )


