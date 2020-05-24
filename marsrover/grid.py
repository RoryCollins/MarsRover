from marsrover.position import Position


class Grid:
    def __init__(self, x, y, *args) -> None:
        self.__x_length = x
        self.__y_length = y
        self.__obstacles = list(args)
        self.__position = Position(0, 0)
        self.__blocked = False

    def get_position(self) -> Position:
        return self.__position

    def move_to(self, position: Position) -> None:
        if position in self.__obstacles:
            self.__blocked = True
        else:
            self.__blocked = False
            self.__position.X = position.X % self.__x_length
            self.__position.Y = position.Y % self.__y_length

    def __str__(self) -> str:
        return "O:{}".format(self.__position) if self.__blocked else "{}".format(self.__position)
