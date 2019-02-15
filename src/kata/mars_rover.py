import abc


class Direction(abc.ABC):

    @classmethod
    def north(cls) -> 'Direction':
        return North()

    @classmethod
    def south(cls) -> 'Direction':
        return South()

    @classmethod
    def east(cls) -> 'Direction':
        return East()

    @classmethod
    def west(cls) -> 'Direction':
        return West()

    @abc.abstractmethod
    def opposite(self) -> 'Direction':
        ...

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Direction):  # pragma: nocover
            return NotImplemented
        return type(self) == type(other)


class North(Direction):

    def opposite(self) -> Direction:
        return Direction.south()


class South(Direction):

    def opposite(self) -> Direction:
        return Direction.north()


class East(Direction):

    def opposite(self) -> Direction:
        return Direction.west()


class West(Direction):

    def opposite(self) -> Direction:
        return Direction.east()


class Location:

    def __init__(self, horizontal: int, vertical: int) -> None:
        self._horizontal = horizontal
        self._vertical = vertical

    def next_in(self, direction: Direction) -> 'Location':
        if direction == Direction.north():
            return self._moved_verticaly_by(-1)
        elif direction == Direction.south():
            return self._moved_verticaly_by(1)
        elif direction == Direction.east():
            return self._moved_horizontaly_by(1)
        else:
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
