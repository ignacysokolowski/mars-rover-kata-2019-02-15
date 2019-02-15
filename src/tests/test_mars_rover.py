class Location:

    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._x!r}, {self._y!r})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Location):  # pragma: nocover
            return NotImplemented
        return self._x == other._x and self._y == other._y


class Rover:

    def __init__(self, initial_position: Location) -> None:
        self._position = initial_position

    def position(self) -> Location:
        return self._position

    def direction(self) -> str:
        return 'N'


class TestRover:

    def test_starts_at_the_given_position(self) -> None:
        rover = Rover(Location(1, 3))
        assert rover.position() == Location(1, 3)

    def test_is_initially_facing_north(self) -> None:
        rover = Rover(Location(1, 3))
        assert rover.direction() == 'N'


class TestLocation:

    def test_two_equal_locations(self) -> None:
        assert Location(0, 0) == Location(0, 0)

    def test_two_locations_with_differrent_x(self) -> None:
        assert Location(0, 0) != Location(1, 0)

    def test_two_locations_with_differrent_y(self) -> None:
        assert Location(0, 0) != Location(0, 1)
