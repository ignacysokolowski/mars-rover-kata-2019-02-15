from typing import Tuple

Location = Tuple[int, int]


class Rover:

    def __init__(self, initial_position: Location) -> None:
        self._position = initial_position

    def position(self) -> Location:
        return self._position


class TestRover:

    def test_starts_at_the_given_position(self) -> None:
        position = (1, 3)
        rover = Rover(position)
        assert rover.position() == position
