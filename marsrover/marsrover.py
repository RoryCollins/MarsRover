from marsrover.command import LeftCommand, RightCommand, MoveCommand
from marsrover.direction import North
from marsrover.position import Position


class MarsRover:
    def __init__(self, grid):
        self.direction = North()
        self.commands = {"L": LeftCommand(), "R": RightCommand(), "M": MoveCommand()}
        self.grid = grid

    def get_location(self):
        return "{}:{}".format(self.grid, self.direction)

    def execute(self, command_list):
        self.validate(command_list)
        for step in list(command_list):
            self.commands[step].execute(self)

    def validate(self, command_list):
        for step in list(command_list):
            if step not in self.commands:
                raise ValueError

    def turn_left(self):
        self.direction = self.direction.turn_left()

    def turn_right(self):
        self.direction = self.direction.turn_right()

    def move(self):
        self.direction.move(self.grid)
