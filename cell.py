from point import Line, Point


class Cell:
    def __init__(self, window, start, end, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.__start = start
        self.__end = end
        self.__window = window

    def draw(self):
        if self.has_left_wall:
            self.__window.draw_line(Line(self.__start, Point(self.__start.x, self.__end.y)), "black")
        if self.has_right_wall:
            self.__window.draw_line(Line(Point(self.__end.x, self.__start.y), self.__end), "black")
        if self.has_top_wall:
            self.__window.draw_line(Line(self.__start, Point(self.__end.x, self.__start.y)), "black")
        if self.has_bottom_wall:
            self.__window.draw_line(Line(Point(self.__start.x, self.__end.y), self.__end), "black")
