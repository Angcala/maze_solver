from cell import Cell
from graphics import Window
from maze import Maze
from point import Line, Point


def main():
    win = Window(800, 600)
    # p1 = Point(0, 0)
    # p2 = Point(100, 100)
# 
    # cell = Cell(win, p1, p2, has_right_wall=False)
    # cell.draw()
    # cell2 = Cell(win, Point(100, 0), Point(200, 100))
    # cell2.draw()
    # cell.draw_move(cell2, undo=True)
    maze = Maze(0, 0, 10, 10, 50, 50, win=win)
  
    win.wait_for_close()

if __name__ == "__main__":
    main()

