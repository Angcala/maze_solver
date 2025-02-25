import time

from cell import Cell
from point import Point


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,     
        ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        # fills in self._cells with lists of cells
        if self.__num_rows <= 0 or self.__num_cols <= 0:
            raise ValueError("num_rows and num_cols must be greater than 0")
        for i in range(self.__num_rows):
            row = []
            for j in range(self.__num_cols):
                start = Point(self.__x1 + j * self.__cell_size_x, self.__y1 + i * self.__cell_size_y)
                end = Point(start.x + self.__cell_size_x, start.y + self.__cell_size_y)
                row.append(Cell(start, end, window=self.__win))
            self._cells.append(row)
    
        if self.__win:
            for row in range(0, len(self._cells)):
                for cell in range(0, len(self._cells[row])):
                    self._draw_cell(row, cell)

    def _draw_cell(self, i, j):
        # draws the cell at row i, column j
        self._cells[i][j].draw()
        self._animate()
    
    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        last_cell = self._cells[-1][-1]
        first_cell.has_left_wall = False
        last_cell.has_right_wall = False
        if self.__win:
            self._draw_cell(0, 0)
            self._draw_cell(self.__num_rows - 1, self.__num_cols - 1)
