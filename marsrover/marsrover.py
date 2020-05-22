from marsrover.command import LeftCommand, RightCommand, MoveCommand
from marsrover.direction import North
from marsrover.position import Position


class MarsRover:
    def __init__(self):
        self.bearing = North()
        self.position = Position(0, 0)
        self.commands = {"L": LeftCommand(), "R": RightCommand(), "M": MoveCommand()}

    def get_location(self):
        return "{}:{}".format(self.position, self.bearing)

    def execute(self, command_list):
        self.validate(command_list)
        for step in list(command_list):
            self.commands[step].execute(self)

    def validate(self, command_list):
        for step in list(command_list):
            if step not in self.commands:
                raise ValueError

    def turn_left(self):
        self.bearing = self.bearing.turn_left()

    def turn_right(self):
        self.bearing = self.bearing.turn_right()

    def move(self):
        self.position = self.bearing.move(self.position)
