import pytest
from marsrover import MarsRover
from marsrover.position import Position
from marsrover.grid import Grid


@pytest.fixture
def curiosity():
    return MarsRover(Grid(10, 10))


def test_rover_has_initial_direction_at_origin(curiosity):
    assert curiosity.get_location() == "0:0:N"


@pytest.mark.parametrize("command, direction", [("L", "W"), ("LL", "S"), ("LLL", "E"), ("LLLL", "N")])
def test_rover_can_turn_left(curiosity, command, direction):
    curiosity.execute(command)
    assert curiosity.get_location() == "0:0:{}".format(direction)


@pytest.mark.parametrize("command, direction", [("R", "E"), ("RR", "S"), ("RRR", "W"), ("RRRR", "N")])
def test_rover_can_turn_right(curiosity, command, direction):
    curiosity.execute(command)
    assert curiosity.get_location() == "0:0:{}".format(direction)


@pytest.mark.parametrize("command, y_position", [("M", "1"), ("MM", "2")])
def test_rover_can_move_forward(curiosity, command, y_position):
    curiosity.execute(command)
    assert curiosity.get_location() == "0:{}:N".format(y_position)


def test_rover_can_traverse_grid(curiosity):
    curiosity.execute("MMRMMLMMLMLM")
    assert curiosity.get_location() == "1:3:S"


@pytest.mark.parametrize("command, location", [("MMMMMMMMMM", "0:0:N"), ("LM", "9:0:W")])
def test_grid_wraps_around(curiosity, command, location):
    curiosity.execute(command)
    assert curiosity.get_location() == location


def test_non_parseable_commands_throw_exception(curiosity):
    with pytest.raises(ValueError):
        curiosity.execute("RMMF")
    assert curiosity.get_location() == "0:0:N"


def test_rover_cannot_move_through_obstacle():
    grid = Grid(10, 10, Position(0, 4))
    curiosity = MarsRover(grid)
    curiosity.execute("MMMMMM")
    assert curiosity.get_location() == "O:0:3:N"


def test_rover_can_move_around_obstacle():
    grid = Grid(10, 10, Position(0, 4))
    curiosity = MarsRover(grid)
    curiosity.execute("MMMMMMRMLMMLMRM")
    assert curiosity.get_location() == "0:6:N"


def test_rover_can_wrap_around_different_sized_grids():
    grid = Grid(5, 8)
    curiosity = MarsRover(grid)
    curiosity.execute("LMLM")
    assert curiosity.get_location() == "4:7:S"