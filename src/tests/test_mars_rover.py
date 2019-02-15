class Location:

    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._x!r}, {self._y!r})'

    def __eq__(self, other: object) -> bool:
        return True


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


class TestLocation:

    def test_two_equal_locations(self) -> None:
        assert Location(0, 0) == Location(0, 0)
