from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    Maze(10,10,10,15,50,50,win)
    win.wait_for_close()

if __name__ == '__main__':
    main()
