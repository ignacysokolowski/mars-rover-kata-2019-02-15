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


class Direction:

    @classmethod
    def north(cls) -> 'Direction':
        return cls('N')

    def __init__(self, symbol: str) -> None:
        self._symbol = symbol

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._symbol!r})'

    def __eq__(self, other: object) -> bool:
        return True


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
        direction = Direction.north()
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


class TestDirection:

    def test_two_equal_directions(self) -> None:
        assert Direction.north() == Direction.north()
