class Direction:

    @classmethod
    def north(cls) -> 'Direction':
        return cls('N')

    @classmethod
    def south(cls) -> 'Direction':
        return cls('S')

    def __init__(self, symbol: str) -> None:
        self._symbol = symbol

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._symbol!r})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Direction):  # pragma: nocover
            return NotImplemented
        return self._symbol == other._symbol


class Location:

    def __init__(self, vertical: int, horizontal: int) -> None:
        self._vertical = vertical
        self._horizontal = horizontal

    def next_in(self, direction: Direction) -> 'Location':
        if direction == Direction.north():
            return self._next_north()
        else:
            return self._next_south()

    def _next_north(self) -> 'Location':
        return Location(self._vertical, self._horizontal - 1)

    def _next_south(self) -> 'Location':
        return Location(self._vertical, self._horizontal + 1)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._vertical!r}, {self._horizontal!r})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Location):  # pragma: nocover
            return NotImplemented
        return self._vertical == other._vertical and self._horizontal == other._horizontal


class Rover:

    def __init__(self, initial_position: Location, initial_direction: Direction) -> None:
        self._position = initial_position
        self._direction = initial_direction

    def move_forward(self) -> None:
        self._position = self._position.next_in(self._direction)

    def position(self) -> Location:
        return self._position

    def direction(self) -> Direction:
        return self._direction


class TestRover:

    def test_starts_at_the_given_position_and_facing_direction(self) -> None:
        rover = Rover(Location(1, 3), Direction.north())
        assert rover.position() == Location(1, 3)
        assert rover.direction() == Direction.north()

    def test_moves_forward_north(self) -> None:
        rover = Rover(Location(3, 3), Direction.north())
        rover.move_forward()
        assert rover.position() == Location(3, 2)

    def test_moves_forward_south(self) -> None:
        rover = Rover(Location(3, 3), Direction.south())
        rover.move_forward()
        assert rover.position() == Location(3, 4)


class TestLocation:

    def test_two_equal_locations(self) -> None:
        assert Location(0, 0) == Location(0, 0)

    def test_two_locations_with_differrent_vertical_position(self) -> None:
        assert Location(0, 0) != Location(1, 0)

    def test_two_locations_with_differrent_horizontal_position(self) -> None:
        assert Location(0, 0) != Location(0, 1)


class TestDirection:

    def test_two_equal_directions(self) -> None:
        assert Direction.north() == Direction.north()

    def test_two_differernt_directions(self) -> None:
        assert Direction.north() != Direction.south()
