from .coordinates import Coordinates
from .direction import Direction


class Rover:

    def __init__(self, initial_position: Coordinates, initial_direction: Direction) -> None:
        self._position = initial_position
        self._direction = initial_direction

    def move_forward(self) -> None:
        self._position = self._position.next_in(self._direction)

    def move_backward(self) -> None:
        self._position = self._position.next_in(self._direction.opposite())

    def turn_right(self) -> None:
        self._direction = self._direction.next_to_the_right()

    def turn_left(self) -> None:
        self._direction = self._direction.next_to_the_left()

    def position(self) -> Coordinates:
        return self._position

    def direction(self) -> Direction:
        return self._direction
