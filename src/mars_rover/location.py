from .direction import Direction


class Step:

    @classmethod
    def north(cls) -> 'Step':
        return cls(0, -1)

    @classmethod
    def south(cls) -> 'Step':
        return cls(0, 1)

    @classmethod
    def east(cls) -> 'Step':
        return cls(1, 0)

    def __init__(self, east: int, south: int) -> None:
        self._east = east
        self._south = south

    def points_south(self) -> int:
        return self._south

    def points_east(self) -> int:
        return self._east


class Location:

    def __init__(self, horizontal: int, vertical: int) -> None:
        self._horizontal = horizontal
        self._vertical = vertical

    def next_in(self, direction: Direction) -> 'Location':
        if direction == Direction.north():
            return self._moved_by(Step.north())
        elif direction == Direction.south():
            return self._moved_by(Step.south())
        elif direction == Direction.east():
            return self._moved_by(Step.east())
        else:
            return self._moved_by(Step(-1, 0))

    def _moved_by(self, step: Step) -> 'Location':
        return Location(
            self._horizontal + step.points_east(),
            self._vertical + step.points_south(),
        )

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._horizontal!r}, {self._vertical!r})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Location):  # pragma: nocover
            return NotImplemented
        return self._horizontal == other._horizontal and self._vertical == other._vertical
