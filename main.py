from cell import Cell
from graphics import Window
from point import Line, Point


def main():
    win = Window(800, 600)
    p1 = Point(10, 10)
    p2 = Point(100, 100)

    cell = Cell(win, p1, p2, has_left_wall=False, has_right_wall=False)
    cell.draw()
    cell2 = Cell(win, Point(200, 200), Point(300, 300), has_top_wall=False, has_bottom_wall=False)
    cell2.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()

