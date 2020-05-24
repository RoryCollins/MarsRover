from abc import ABC, abstractmethod

from marsrover.position import Position


class Direction(ABC):
    @abstractmethod
    def turn_left(self):
        pass

    @abstractmethod
    def turn_right(self):
        pass

    @abstractmethod
    def move(self, current_position):
        pass

    @abstractmethod
    def __str__(self):
        pass


class North(Direction):
    def __str__(self):
        return "N"

    def turn_left(self):
        return West()

    def turn_right(self):
        return East()

    def move(self, grid):
        grid.move_to(Position(grid.get_position().X, grid.get_position().Y + 1))


class West(Direction):
    def __str__(self):
        return "W"

    def turn_left(self):
        return South()

    def turn_right(self):
        return North()

    def move(self, grid):
        grid.move_to(Position(grid.get_position().X - 1, grid.get_position().Y))


class East(Direction):
    def __str__(self):
        return "E"

    def turn_left(self):
        return North()

    def turn_right(self):
        return South()

    def move(self, grid):
        grid.move_to(Position(grid.get_position().X + 1, grid.get_position().Y))


class South(Direction):
    def __str__(self):
        return "S"

    def turn_left(self):
        return East()

    def turn_right(self):
        return West()

    def move(self, grid):
        grid.move_to(Position(grid.get_position().X, grid.get_position().Y - 1))
