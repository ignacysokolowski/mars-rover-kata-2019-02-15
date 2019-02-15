class Location:

    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y


class Rover:

    def __init__(self, initial_position: Location) -> None:
        self._position = initial_position

    def position(self) -> Location:
        return self._position


class TestRover:

    def test_starts_at_the_given_position(self) -> None:
        position = Location(1, 3)
        rover = Rover(position)
        assert rover.position() == position
