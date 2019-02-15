class Direction:

    @classmethod
    def north(cls) -> 'Direction':
        return North()

    @classmethod
    def south(cls) -> 'Direction':
        return cls('S')

    @classmethod
    def east(cls) -> 'Direction':
        return cls('E')

    @classmethod
    def west(cls) -> 'Direction':
        return cls('W')

    def __init__(self, symbol: str) -> None:
        self._symbol = symbol

    def opposite(self) -> 'Direction':
        if self == Direction.south():
            return Direction.north()
        elif self == Direction.east():
            return Direction.west()
        else:
            return Direction.east()

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._symbol!r})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Direction):  # pragma: nocover
            return NotImplemented
        return self._symbol == other._symbol


class North(Direction):

    def __init__(self) -> None:
        self._symbol = 'N'

    def opposite(self) -> 'Direction':
        return Direction.south()


class Location:

    def __init__(self, horizontal: int, vertical: int) -> None:
        self._horizontal = horizontal
        self._vertical = vertical

    def next_in(self, direction: Direction) -> 'Location':
        if direction == Direction.north():
            return self._next_north()
        elif direction == Direction.south():
            return self._next_south()
        elif direction == Direction.east():
            return self._next_east()
        else:
            return self._next_west()

    def _next_north(self) -> 'Location':
        return self._moved_verticaly_by(-1)

    def _next_south(self) -> 'Location':
        return self._moved_verticaly_by(1)

    def _next_east(self) -> 'Location':
        return self._moved_horizontaly_by(1)

    def _next_west(self) -> 'Location':
        return self._moved_horizontaly_by(-1)

    def _moved_horizontaly_by(self, points: int) -> 'Location':
        return Location(self._horizontal + points, self._vertical)

    def _moved_verticaly_by(self, points: int) -> 'Location':
        return Location(self._horizontal, self._vertical + points)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._horizontal!r}, {self._vertical!r})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Location):  # pragma: nocover
            return NotImplemented
        return self._horizontal == other._horizontal and self._vertical == other._vertical


class Rover:

    def __init__(self, initial_position: Location, initial_direction: Direction) -> None:
        self._position = initial_position
        self._direction = initial_direction

    def move_forward(self) -> None:
        self._position = self._position.next_in(self._direction)

    def move_backward(self) -> None:
        self._position = self._position.next_in(self._direction.opposite())

    def position(self) -> Location:
        return self._position

    def direction(self) -> Direction:
        return self._direction
