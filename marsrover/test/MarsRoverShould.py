from marsrover import MarsRover
import pytest


def test_rover_has_initial_bearing_at_origin():
    curiosity = MarsRover()
    assert curiosity.get_location() == "0:0:N"


@pytest.mark.parametrize("command, bearing", [("L", "W"), ("LL", "S"), ("LLL", "E"), ("LLLL", "N")])
def test_rover_can_turn_left(command, bearing):
    curiosity = MarsRover()
    curiosity.execute(command)
    assert curiosity.get_location() == "0:0:{}".format(bearing)


@pytest.mark.parametrize("command, bearing", [("R", "E"), ("RR", "S"), ("RRR", "W"), ("RRRR", "N")])
def test_rover_can_turn_right(command, bearing):
    curiosity = MarsRover()
    curiosity.execute(command)
    assert curiosity.get_location() == "0:0:{}".format(bearing)


@pytest.mark.parametrize("command, y_position", [("M", "1"), ("MM", "2")])
def test_rover_can_move_forward(command, y_position):
    curiosity = MarsRover()
    curiosity.execute(command)
    assert curiosity.get_location() == "0:{}:N".format(y_position)


def test_rover_can_traverse_grid():
    curiosity = MarsRover()
    curiosity.execute("MMRMMLMMLMLM")
    assert curiosity.get_location() == "1:3:S"


@pytest.mark.parametrize("command, location", [("MMMMMMMMMM", "0:0:N"), ("LM", "9:0:W")])
def test_grid_wraps_around(command, location):
    curiosity = MarsRover()
    curiosity.execute(command)
    assert curiosity.get_location() == location


def test_non_parseable_commands_throw_exception():
    with pytest.raises(ValueError):
        curiosity = MarsRover()
        curiosity.execute("RMMF")
    assert curiosity.get_location() == "0:0:N"
