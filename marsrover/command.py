from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, rover):
        pass


class LeftCommand(Command):
    def execute(self, rover):
        rover.turn_left()


class RightCommand(Command):
    def execute(self, rover):
        rover.turn_right()


class MoveCommand(Command):
    def execute(self, rover):
        rover.move()
