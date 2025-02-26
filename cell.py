from point import Line, Point


class Cell:
    def __init__(self, start, end, window=None, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.__start = start
        self.__end = end
        self.__window = window
        self.visited = False

    def draw(self):
        if self.has_left_wall:
            self.__window.draw_line(Line(self.__start, Point(self.__start.x, self.__end.y)), "black")
        else:
            self.__window.draw_line(Line(self.__start, Point(self.__start.x, self.__end.y)), "white")
        if self.has_right_wall:
            self.__window.draw_line(Line(Point(self.__end.x, self.__start.y), self.__end), "black")
        else:
            self.__window.draw_line(Line(Point(self.__end.x, self.__start.y), self.__end), "white")
        if self.has_top_wall:
            self.__window.draw_line(Line(self.__start, Point(self.__end.x, self.__start.y)), "black")
        else:
            self.__window.draw_line(Line(self.__start, Point(self.__end.x, self.__start.y)), "white")
        if self.has_bottom_wall:
            self.__window.draw_line(Line(Point(self.__start.x, self.__end.y), self.__end), "black")
        else:
            self.__window.draw_line(Line(Point(self.__start.x, self.__end.y), self.__end), "white")

    def draw_move(self, to_cell, undo=False):
        center_of_cell = Point((self.__start.x + self.__end.x) // 2, (self.__start.y + self.__end.y) // 2)
        center_of_target = Point((to_cell.__start.x + to_cell.__end.x) // 2, (to_cell.__start.y + to_cell.__end.y) // 2)
        
        if undo:
            self.__window.draw_line(Line(Point(center_of_cell.x, center_of_cell.y), Point(center_of_target.x, center_of_target.y)), "gray")
        else:
            self.__window.draw_line(Line(Point(center_of_cell.x, center_of_cell.y), Point(center_of_target.x, center_of_target.y)), "red")
