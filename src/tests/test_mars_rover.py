from typing import Tuple


class Rover:

    def __init__(self, initial_position: Tuple[int, int]) -> None:
        self._position = initial_position

    def position(self) -> Tuple[int, int]:
        return self._position


class TestRover:

    def test_starts_at_the_given_position(self) -> None:
        rover = Rover((1, 3))
        assert rover.position() == (1, 3)
