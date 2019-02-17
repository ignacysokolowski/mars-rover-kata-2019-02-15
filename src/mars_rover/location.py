from .direction import Direction


class Step:

    def __init__(self, south: int) -> None:
        self._south = south

    def points_south(self) -> int:
        return self._south


class Location:

    def __init__(self, horizontal: int, vertical: int) -> None:
        self._horizontal = horizontal
        self._vertical = vertical

    def next_in(self, direction: Direction) -> 'Location':
        if direction == Direction.north():
            return self._moved_by(Step(-1))
        elif direction == Direction.south():
            return self._moved_verticaly_by(1)
        elif direction == Direction.east():
            return self._moved_horizontaly_by(1)
        else:
            return self._moved_horizontaly_by(-1)

    def _moved_by(self, step: Step) -> 'Location':
        return Location(self._horizontal, self._vertical + step.points_south())

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
