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


Direction = str


class Rover:

    def __init__(self, initial_position: Location, initial_direction: Direction) -> None:
        self._position = initial_position
        self._direction = initial_direction

    def position(self) -> Location:
        return self._position

    def direction(self) -> Direction:
        return self._direction


class TestRover:

    def test_starts_at_the_given_position_and_facing_direction(self) -> None:
        direction = Direction('N')
        rover = Rover(Location(1, 3), direction)
        assert rover.position() == Location(1, 3)
        assert rover.direction() == direction


class TestLocation:

    def test_two_equal_locations(self) -> None:
        assert Location(0, 0) == Location(0, 0)

    def test_two_locations_with_differrent_x(self) -> None:
        assert Location(0, 0) != Location(1, 0)

    def test_two_locations_with_differrent_y(self) -> None:
        assert Location(0, 0) != Location(0, 1)
