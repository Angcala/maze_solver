import random
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
            seed=None,     
        ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            neighbor_cells = self._get_neighbors(i, j)
            for neighbor_coords in neighbor_cells:
                if not self._cells[neighbor_coords[0]][neighbor_coords[1]].visited:
                    to_visit.append(neighbor_coords)
            if not to_visit:
                if self.__win:
                    self._draw_cell(i, j)
                return
            next_cell_coords = random.choice(to_visit)
            # break the walls between the two cells
            if next_cell_coords[0] > i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_cell_coords[0]][next_cell_coords[1]].has_top_wall = False
            elif next_cell_coords[0] < i:
                self._cells[i][j].has_top_wall = False
                self._cells[next_cell_coords[0]][next_cell_coords[1]].has_bottom_wall = False
            elif next_cell_coords[1] > j:
                self._cells[i][j].has_right_wall = False
                self._cells[next_cell_coords[0]][next_cell_coords[1]].has_left_wall = False
            elif next_cell_coords[1] < j:
                self._cells[i][j].has_left_wall = False
                self._cells[next_cell_coords[0]][next_cell_coords[1]].has_right_wall = False
            
            if self.__win:
                self._draw_cell(i, j)
                self._draw_cell(next_cell_coords[0], next_cell_coords[1])
            self._break_walls_r(next_cell_coords[0], next_cell_coords[1])

    def _get_neighbors(self, i, j):
        neighbors = []
        if i > 0:
            neighbors.append((i - 1, j))
        if i < self.__num_rows - 1:
            neighbors.append((i + 1, j))
        if j > 0:
            neighbors.append((i, j - 1))
        if j < self.__num_cols - 1:
            neighbors.append((i, j + 1))
        return neighbors

    def _reset_cells_visited(self):
        print("resetting cells visited...")
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[-1][-1]:
            return True
        neighbors = self._get_neighbors(i, j)
        for neighbor_coords in neighbors:
            target_cell = self._cells[neighbor_coords[0]][neighbor_coords[1]]
            # figure out which direction the cell is in
            has_wall = False
            if neighbor_coords[0] > i:
                has_wall = target_cell.has_top_wall
            elif neighbor_coords[0] < i:
                has_wall = target_cell.has_bottom_wall
            elif neighbor_coords[1] > j:
                has_wall = target_cell.has_left_wall
            elif neighbor_coords[1] < j:
                has_wall = target_cell.has_right_wall
            
            if not has_wall and not target_cell.visited:
                self._cells[i][j].draw_move(target_cell)
                if self._solve_r(neighbor_coords[0], neighbor_coords[1]):
                    return True
                self._cells[i][j].draw_move(target_cell, undo=True)
        return False
