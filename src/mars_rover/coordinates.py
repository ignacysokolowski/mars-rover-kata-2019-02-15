from .direction import Direction
from .step import Step


class Coordinates:

    def __init__(self, horizontal: int, vertical: int) -> None:
        if horizontal < 0:
            raise ValueError()
        self._horizontal = horizontal
        self._vertical = vertical

    def next_in(self, direction: Direction) -> 'Coordinates':
        return self._moved_by(direction.step())

    def _moved_by(self, step: Step) -> 'Coordinates':
        return Coordinates(
            self._horizontal + step.points_east(),
            self._vertical + step.points_south(),
        )

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._horizontal!r}, {self._vertical!r})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinates):  # pragma: nocover
            return NotImplemented
        return self._horizontal == other._horizontal and self._vertical == other._vertical
